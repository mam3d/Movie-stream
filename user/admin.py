from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["phone","name","is_staff","is_admin"]
    list_filter = ["is_staff","is_admin"]
    ordering = ["name"]
    fieldsets = (
        (None, {
            "fields": (
                "phone","name","password","is_staff","is_admin"
            ),
        }),
    )
    
