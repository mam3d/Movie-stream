import random
from django.http import Http404
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import (
        generics,
        status,
        permissions,
        views,
        response,
        authentication
        )
from user.tasks import subscription_expire
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
            PhoneVerifySerializer,
            UserRegisterSerializer,
            LoginSerializer,
            UserProfileSerializer,
            SubscriptionViewSerializer,
            SubscriptionOrderSerializer
            )
from ..models import (
    CustomUser,
    PhoneVerify,
    Subscription,
    UserSubscription,
    UserOrder,
    DoublePay
    )
from ..helpers import (
    send_smscode,
    pay_with_idpay
    )

class PhoneVerifyCreate(generics.CreateAPIView):
    serializer_class = PhoneVerifySerializer

    def create(self,request,*args, **kwargs):
        super().create(request,*args, **kwargs)
        return response.Response(
            {"success":"code has been sent to your phone"},
            status=status.HTTP_201_CREATED
            )

    def perform_create(self, serializer):
        phone = serializer.validated_data.get("phone")
        code = random.randint(9999,99999)
        phone_queryset = PhoneVerify.objects.filter(phone=phone)
        if phone_queryset.exists():
            phone_verify = phone_queryset[0]
            phone_verify.code = code
            phone_verify.count += 1
            phone_verify.save()
            # send_smscode(code,phone)
        else:      
            serializer.save(code=code)
            # send_smscode(code,phone)

class RegisterView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        refresh = RefreshToken.for_user(user)
        return response.Response(
            {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
            },
        status = status.HTTP_201_CREATED
        )
        

    def perform_create(self, serializer):
        user = serializer.save()
        return user


class LoginView(views.APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.validated_data)
        return response.Response({
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        })

class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = None
    serializer_class = UserProfileSerializer

    def get_object(self):
        return CustomUser.objects.get(phone=self.request.user)


class SubscriptionView(generics.ListAPIView):
    serializer_class = SubscriptionViewSerializer
    queryset = Subscription.objects.all()


class SubscriptionOrderView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SubscriptionOrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            subscription_id = serializer.validated_data["subscription_id"]
            user = serializer.validated_data["user"]
            result = pay_with_idpay(subscription_id, user)

            double_pay = DoublePay.objects.create(user=request.user, idpay_id=result["id"])

            return response.Response(result["link"])
        return response.Response(serializer.errors)

    def get(self,request):
        double_pay = get_object_or_404(DoublePay, user=request.user)
        idpay_id = request.GET.get("id")
        if idpay_id is None:
            raise Http404

        if int(request.GET.get("status")) == 10 and double_pay.idpay_id == idpay_id:

            order_id = request.get("order_id")
            subscription = Subscription.objects.get(id=int(order_id))
            user_subscription = UserSubscription.objects.get(user=request.user)
            user_subscription.subscription = subscription
            user_subscription.date_joined = timezone.now()
            user_subscription.save()

            UserOrder.objects.create(
                    user = request.user,
                    track_id = request.GET.get("track_id"),
                    order = subscription,
                    )
            double_pay.delete()

            subscription_expire.apply_async(
                (user_subscription.id,),
                eta=user_subscription.date_expires
                )

            return response.Response("thanks for your purchase")
        return response.Response("purchase failed")