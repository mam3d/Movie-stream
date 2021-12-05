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
    list_filter = ["category"]
    prepopulated_fields = ({"slug":("name",)})
    raw_id_fields = ["category","actor"]

admin.site.register(Actor)

