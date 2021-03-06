from django.test import TestCase
from user.models import (
        CustomUser,
        Subscription
        )
from ..models import (
        Category,
        Movie,
        Actor,
        Rating
        )


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name = "ps5 test"
        )
    
    def test_category_created(self):
        self.assertEqual(self.category.name,"ps5 test")
        self.assertEqual(self.category.slug,"ps5-test")
        self.assertEqual(str(self.category),"ps5 test")


class MovieTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name = "Horror"
        )
        category2 = Category.objects.create(
            name = "Comedy"
        )
        actor = Actor.objects.create(name="test actor")
        self.movie = Movie.objects.create(
            name = "chucky",
            image = "media/chucky.png",
            )
        self.movie.categories.add(category,category2)
        self.movie.actors.add(actor)
        self.category_count = self.movie.categories.count()
        self.actor_count = self.movie.actors.count()

    def test_movie_created(self):
        self.assertEqual(self.movie.name,"chucky")
        self.assertEqual(self.movie.slug,"chucky")
        self.assertEqual(self.category_count,2)
        self.assertEqual(self.actor_count,1)
        self.assertEqual(self.movie.image,"media/chucky.png")
        self.assertEqual(str(self.movie),"chucky")


class ActorTest(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name="test actor")
    
    def test_actor_created(self):
        self.assertEqual(self.actor.name,"test actor")
        self.assertEqual(str(self.actor),"test actor")


class RatingTest(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(
            phone = "09026673395",
            password = "imtestingit",
            )
        movie = Movie.objects.create(
            name = "chucky",
            image = "media/chucky.png",
            )
        self.rating = Rating.objects.create(user=user,movie=movie,number=10)
    
    def test_rating_created(self):
        self.assertEqual(self.rating.user.phone,"09026673395")
        self.assertEqual(self.rating.movie.name,"chucky")
        self.assertEqual(str(self.rating),"09026673395's rate")
