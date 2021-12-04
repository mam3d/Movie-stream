from django.test import TestCase
from ..models import (
    UserSubscription,
    CustomUser,
    Subscription
    )

class CreateUserSubscriptionSignalTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name="F",price=0)
        self.user = CustomUser.objects.create_user(
            phone = "09026673395",
            password = "imtestingit"
        )

    def test_signal(self):
        user_subscription = UserSubscription.objects.filter(user=self.user)
        self.assertTrue(user_subscription)