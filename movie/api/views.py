from rest_framework import generics
from .serializers import (
        CategorySerializer,
        )
from ..models import (
        Category,
        )


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"