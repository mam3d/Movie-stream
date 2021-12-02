from rest_framework import serializers
from ..models import (
        PhoneVerify,
        CustomUser,
        )
from ..validators import phone_validator



class PhoneVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerify
        fields = ["phone"]
    
    def validate_phone(self,value):
        phone = phone_validator(value)
        user = CustomUser.objects.filter(phone=phone)
        if user:
            raise serializers.ValidationError("user with this phone number exists")
            
        phone_queryset = PhoneVerify.objects.filter(phone=phone)
        if phone_queryset.exists():
            phone_verify = phone_queryset.first()
            if phone_verify.count >= 8:
                raise serializers.ValidationError("you cant request code anymore")
            return phone
        return phone

        
        
        
