from django.test import TestCase
from ..models import (
            Category,
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
