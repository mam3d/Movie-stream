from django.test import TestCase
from user.api.serializers import (
            PhoneVerifySerializer,
            UserRegisterSerializer,
            LoginSerializer,
            )
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
        CustomUser.objects.create_user(
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


class UserRegisterSerializerTest(TestCase):
    def setUp(self):
        PhoneVerify.objects.create(
            phone = "09026673395",
            code = 123456,
            )

    def test_is_valid(self):
        data = {
            "phone":"09026673395",
            "password":"imtestingit",
            "password2":"imtestingit",
            "code":123456
        }
        serializer = UserRegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_not_valid(self):
        data = {
            "phone":"09026673395",
            "password":"imtestingit",
            "password2":"124141441",
            "code":12355,
        }
        serializer = UserRegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_not_valid2(self):
        data = {
            "phone":"09026673395",
            "password":"imtestingit",
            "password2":"imtestingit",
            "code":000000, # wrong code
        }
        serializer = UserRegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class LoginSerializerTest(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
                phone = "09026673395",
                password = "imtestingit"
                )

    def test_is_valid(self):
        data = {
            "phone":"09026673395",
            "password":"imtestingit",
        }
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_not_valid(self):
        data = {
            "phone":"09010000000", #wrong phone
            "password":"imtestingit",
        }
        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())