from django.test import TestCase
from ..models import CustomUser


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
