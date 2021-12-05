from django.contrib import admin
from .models import (
        Category,
        Movie,
        Actor
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = ({"slug":("name",)})

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_filter = ["categories"]
    prepopulated_fields = ({"slug":("name",)})
    raw_id_fields = ["categories","actors"]

admin.site.register(Actor)

