from django.contrib import admin
from .models import (
        Category,
        Movie,
        Actor,
        Rating
)

admin.site.register(Actor)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = ({"slug":("name",)})

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name","rating"]
    list_filter = ["categories"]
    prepopulated_fields = ({"slug":("name",)})
    raw_id_fields = ["categories","actors"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["user","movie","number"]
    list_filter = ["user","movie"]

