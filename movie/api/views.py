from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user.api.permissions import SubscriptionPermission
from .serializers import (
        CategorySerializer,
        MovieListSerializer,
        MovieDetailSerializer
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


class MovieDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,SubscriptionPermission]
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = "slug"   
