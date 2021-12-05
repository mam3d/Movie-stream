from django.urls import path
from .views import (
    CategoryDetail,
    MovieList,
    )

urlpatterns = [
    path("category/<slug:slug>/",CategoryDetail.as_view(),name="category_detail"),
    path("movies/",MovieList.as_view(),name="movies"),
]
