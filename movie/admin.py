from django.contrib import admin
from .models import (
        Category,
        Movie,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = ({"slug":("name",)})
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name","categories"]
    list_filter = ["category"]
