from django.test import TestCase
from django.urls import reverse
from ..models import PhoneVerify


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