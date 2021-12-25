from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import (
        PhoneVerify,
        CustomUser,
        Subscription
        )



class PhoneVerifyCreateTest(APITestCase):
    def setUp(self):
        self.url = reverse("validate_phone")

    def test_create(self):
        data = {
            "phone":"09026673395"
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_not_create(self):
        data = {
            "phone":"09026asfa673395"
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_phone_queryset_exists(self):
        PhoneVerify.objects.create(
            phone = "09036673395",
            code = 45656,
            count = 1
            )
        data = {
            "phone":"09036673395"
        }
        response = self.client.post(self.url, data=data, format="json")
        phone = PhoneVerify.objects.get(phone="09036673395")
        self.assertEqual(phone.count,2)
        self.assertEqual(response.status_code,201)


class UserRegisterViewTest(APITestCase):
    def setUp(self):
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
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_not_create(self):
        data = {
            "phone":"09026asfa673395",
            "password":"imtestingit",
            "password2":"oafasflkafsf",
            "code":00000,
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, 400)

class ProfileViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("profile")
        user = CustomUser.objects.create_user(
                        phone = "09026673395",
                        password = "testing321",
                        )
        self.refresh = RefreshToken.for_user(user)

    def test_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)


class SubscriptionViewTest(APITestCase):
    def setUp(self):
        self.url = reverse("subscriptions")
        self.subscription = Subscription.objects.create(
                name = "P",
                price = 50,
                month = 1,
                )

    def test_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "pro")

