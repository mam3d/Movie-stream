from django.urls import path
from .views import PhoneVerifyCreate

urlpatterns = [
    path("validate-phone/",PhoneVerifyCreate.as_view(),name="validate_phone")
]
