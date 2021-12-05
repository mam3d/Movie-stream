from django.test import TestCase
from ..models import (
        Category,
        Movie,
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
        self.movie = Movie(
            name = "chucky",
            image = "media/chucky.png",
            )
        self.movie.save()
        self.movie.category.add(category,category2)
    
    def test_movie_created(self):
        self.assertEqual(self.movie.name,"chucky")
        self.assertEqual(self.movie.slug,"chucky")
        self.assertEqual(self.movie.categories,"Horror Comedy ")
        self.assertEqual(str(self.movie),"chucky")
