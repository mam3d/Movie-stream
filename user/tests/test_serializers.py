from django.test import TestCase
from user.api.serializers import PhoneVerifySerializer
from ..models import (
        CustomUser,
        PhoneVerify,
        )


class PhoneVerifySerializerTest(TestCase):
    def test_is_valid(self):
        data = {
            "phone":"09036673395"
        }
        serializer = PhoneVerifySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_not_valid(self):
        data = {
            "phone":"0903ss6673395"
        }
        serializer = PhoneVerifySerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_not_valid_user_exists(self):
        user = CustomUser.objects.create_user(
            phone = "09026673395",
            password = "imtestingit"
            )
        data = {
            "phone":"09026673395"
        }
        serializer = PhoneVerifySerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_not_valid_phone_verify_limit(self):
        PhoneVerify.objects.create(
            phone = "09026673395",
            code = 1213913,
            count = 8
        )
        data = {
            "phone":"09026673395"
        }
        serializer = PhoneVerifySerializer(data=data)
        self.assertFalse(serializer.is_valid())