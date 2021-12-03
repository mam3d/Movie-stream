from django.test import TestCase
from django.core.exceptions import ValidationError
from ..validators import (
            phone_validator,
            check_user_not_exists,
            )
from ..models import CustomUser


class PhoneValidatorTest(TestCase):

    def test_raise(self):
        with self.assertRaises(ValidationError):
            phone_validator("092asasa02asg5")
    
    def test_returend_data(self):
        phone = phone_validator("09026673395")
        self.assertEqual(phone,"09026673395")


class CheckUserNotExitsTest(TestCase):

    def test_raise(self):
        CustomUser.objects.create_user(phone="09026673395",password="imtestingit")
        with self.assertRaises(ValidationError):
            check_user_not_exists("09026673395")
    
    def test_returend_data(self):
        phone = check_user_not_exists("09026673395")
        self.assertEqual(phone,"09026673395")