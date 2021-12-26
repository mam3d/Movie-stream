from django.contrib.auth import authenticate
from django.core.cache import cache
from rest_framework import serializers, validators
from rest_framework.fields import CurrentUserDefault
from ..models import (
        CustomUser,
        Subscription,
        UserSubscription
        )
from ..validators import (
    phone_validator,
    check_user_not_exists,
    )



class PhoneVerifySerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, validators=[phone_validator, check_user_not_exists])

    

        
class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()
    password2 = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ["phone","password","password2","code"]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].validators.extend([phone_validator])

    def validate_phone(self,value):
        phoneotp = cache.get(value)
        if phoneotp is None:
            raise serializers.ValidationError("you must verify your phone first")
        return value


        
    def validate(self,data):
        phone = data.get("phone")
        password = data.get("password")
        password2 = data.get("password2")
        code = data.get("code")
        phoneotp_code = cache.get(phone)
        if password != password2:
            raise serializers.ValidationError("passwords didnt match!")
        elif code != phoneotp_code:
            raise serializers.ValidationError("wrong code")
        return data

    def save(self):
        phone = self.validated_data["phone"]
        password = self.validated_data["password"]
        user = CustomUser.objects.create_user(
            phone = phone,
            password = password
        )
        cache.delete(phone)
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator])
    password = serializers.CharField()

    def validate(self,data):
        phone = data.get("phone")
        password = data.get("password")
        user = authenticate(username=phone,password=password)
        if user is None:
            raise serializers.ValidationError("phone number or password is inccorect")
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()
    date_expires = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ["phone","name","subscription","date_expires"]

    def get_subscription(self,obj):
        return obj.user_subscription.subscription.get_name_display()

    def get_date_expires(self,obj):
        return obj.user_subscription.date_expires


class SubscriptionViewSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Subscription
        fields = ["id","name","month","price"]
    
    def get_name(self,obj):
        return obj.get_name_display()


class SubscriptionOrderSerializer(serializers.ModelSerializer):
    subscription_id = serializers.IntegerField()

    class Meta:
        model = UserSubscription
        fields = ["subscription_id","user"]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].default = CurrentUserDefault()
        self.fields["user"].required = False

    def validate_subscription_id(self,value):
        subscription_queryset = Subscription.objects.filter(id=value)
        if not subscription_queryset:
            raise serializers.ValidationError("this subscription dose not exist")
        elif subscription_queryset[0].name == "F":
            raise serializers.ValidationError("you cant buy free subscription")
        return value

    def validate_user(self,value):
        if value.user_subscription.subscription.name == "P":
            raise serializers.ValidationError("you should wait your current subscription  has not ended yet")
        return value
        
            


