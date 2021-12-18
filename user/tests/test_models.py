from django.test import TestCase
from ..models import (
            CustomUser,
            PhoneVerify,
            Subscription,
            )


class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            phone = "09026673395",
            password = "imtestingit",
            )
        

    def test_user_created(self):
        self.assertEqual(self.user.phone,"09026673395")
        self.assertTrue(self.user.check_password("imtestingit"))
        self.assertEqual(str(self.user),"09026673395")

    def test_str_with_name(self):
        user = CustomUser(phone="09036673395",password="imtestingit")
        user.name = "mam3d"
        user.save()
        self.assertEqual(str(user),"mam3d")

class PhoneVerifyTest(TestCase):
    def setUp(self):
        self.phone_verify = PhoneVerify.objects.create(
            phone = "09026673395",
            code = 12345,
            count = 1
            )

    def test_phone_verify_created(self):
        self.assertEqual(self.phone_verify.phone,"09026673395")
        self.assertEqual(self.phone_verify.code,12345)
        self.assertEqual(self.phone_verify.count,1)
        self.assertEqual(str(self.phone_verify),"09026673395")

class SubscriptionTest(TestCase):
    def setUp(self):
        self.subscription = Subscription.objects.create(
            name = "P",
            price = 30,
            )

    def test_subscription_created(self):
        self.assertEqual(self.subscription.name,"P")
        self.assertEqual(self.subscription.price,30)
        self.assertEqual(str(self.subscription),"pro")






