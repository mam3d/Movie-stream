from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user.api.permissions import SubscriptionPermission
from .serializers import (
        CategorySerializer,
        MovieListSerializer,
        MovieDetailSerializer,
        RatingSerializer
        )
from ..models import (
        Category,
        Movie,
        Rating
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


class RatingCreate(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated,SubscriptionPermission]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)   
