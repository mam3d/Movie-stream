from django.test import TestCase
from django.urls import reverse
from ..models import (
            Category,
            )



class CategoryDetailTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")

    def test_retrieve(self):
        url = reverse("category_detail",kwargs={"slug":self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_unAuthenticated(self):
        url = reverse("category_detail",kwargs={"slug":"wrong"})
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
