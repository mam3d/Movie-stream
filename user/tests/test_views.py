from django.test import TestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import (
        PhoneVerify,
        Subscription,
        CustomUser
        )


class PhoneVerifyCreateTest(TestCase):
    def setUp(self):
        self.url = reverse("validate_phone")

    def test_create(self):
        data = {
            "phone":"09026673395"
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,201)

    def test_not_create(self):
        data = {
            "phone":"09026asfa673395"
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,400)

    def test_phone_queryset_exists(self):
        PhoneVerify.objects.create(
            phone = "09036673395",
            code = 45656,
            count = 1
            )
        data = {
            "phone":"09036673395"
        }
        response = self.client.post(self.url,data=data)
        phone = PhoneVerify.objects.get(phone="09036673395")
        self.assertEqual(phone.count,2)
        self.assertEqual(response.status_code,201)


class UserRegisterViewTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name="F",price=0)
        self.url = reverse("register")
        self.phone = PhoneVerify.objects.create(
                        phone = "09026673395",
                        code = 123456,
                        )

    def test_create(self):
        data = {
            "phone":"09026673395",
            "password":"imtestingit",
            "password2":"imtestingit",
            "code":123456.
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,201)

    def test_not_create(self):
        data = {
            "phone":"09026asfa673395",
            "password":"imtestingit",
            "password2":"oafasflkafsf",
            "code":00000,
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,400)


