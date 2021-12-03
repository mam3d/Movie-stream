from django.urls import path
from .views import PhoneVerifyCreate, UserRegisterView

urlpatterns = [
    path("validate-phone/",PhoneVerifyCreate.as_view(),name="validate_phone"),
    path ("register/",UserRegisterView.as_view(),name="register")
]
