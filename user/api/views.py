import random
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
            PhoneVerifySerializer,
            UserRegisterSerializer,
            )
from ..models import PhoneVerify
from ..helpers import send_smscode




class PhoneVerifyCreate(generics.CreateAPIView):
    serializer_class = PhoneVerifySerializer

    def create(self,request,*args, **kwargs):
        super().create(request,*args, **kwargs)
        return Response({"success":"code has been sent to your phone"},status=status.HTTP_201_CREATED)

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

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self,request,*args, **kwargs):
        super().create(request,*args, **kwargs)
        return Response({"success":"user has been created"},status=status.HTTP_201_CREATED)

