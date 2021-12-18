from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
        CustomUser,
        PhoneVerify,
        Subscription,
        UserSubscription,
        )


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
    add_fieldsets = (
        (None, {
            "fields": (
                "phone","name","password","is_staff","is_admin"
            ),
        }),
    )

@admin.register(PhoneVerify)
class PhoneVerifyAdmin(admin.ModelAdmin):
    list_display = ["phone","code","count"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["name","price","month"]
    

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user","subscription","date_joined","date_expires"]
    fields = ["user","subscription"]



