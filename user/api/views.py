import random
from rest_framework import (
        generics,
        status,
        permissions,
        views,
        response
        )
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
            PhoneVerifySerializer,
            UserRegisterSerializer,
            LoginSerializer,
            UserProfileSerializer,
            SubscriptionSerializer
            )
from ..models import (
    CustomUser,
    PhoneVerify,
    Subscription,
    )
from ..helpers import send_smscode


class PhoneVerifyCreate(generics.CreateAPIView):
    serializer_class = PhoneVerifySerializer

    def create(self,request,*args, **kwargs):
        super().create(request,*args, **kwargs)
        return response.Response({"success":"code has been sent to your phone"},status=status.HTTP_201_CREATED)

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
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()