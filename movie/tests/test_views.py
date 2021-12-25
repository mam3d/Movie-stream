from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import (
            CustomUser,
            Subscription,
            UserSubscription
            )
from ..models import (
            Category,
            Movie
            )



class CategoryDetailTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")

    def test_retrieve(self):
        url = reverse("category_detail", kwargs={"slug":self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_not_exists(self):
        url = reverse("category_detail", kwargs={"slug":"wrong"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class MovieListTest(APITestCase):
    def setUp(self):
        self.url = reverse("movies")

    def test_retrieve(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class MovieDetailTest(APITestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(
            phone = "09026673395",
            password = "imtestingit",
            )
            
        # change user subscription to pro in order to pass subscription permission
        sub2 = Subscription.objects.create(name="P",price=0)
        user_subscription = UserSubscription.objects.get(user__phone=user)
        user_subscription.subscription = sub2
        user_subscription.save()

        self.refresh = RefreshToken.for_user(user)

        self.movie = Movie.objects.create(name="test",image="test.png")

    def test_retrieve(self):
        url = reverse("movie_detail", kwargs={"slug":self.movie.slug})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_not_exists(self):
        url = reverse("movie_detail",kwargs={"slug":"wrong"})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_not_unAuthenticated(self):
        url = reverse("movie_detail",kwargs={"slug":self.movie.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
