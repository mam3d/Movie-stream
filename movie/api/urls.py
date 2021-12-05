from django.urls import path
from .views import (
    CategoryDetail,
    MovieList,
    MovieDetail,
    )

urlpatterns = [
    path("category/<slug:slug>/",CategoryDetail.as_view(),name="category_detail"),
    path("movies/",MovieList.as_view(),name="movies"),
    path("movie/<slug:slug>/",MovieDetail.as_view(),name="movie_detail"),
]
