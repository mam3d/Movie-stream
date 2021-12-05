from rest_framework import generics
from .serializers import (
        CategorySerializer,
        MovieListSerializer
        )
from ..models import (
        Category,
        Movie
        )


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
