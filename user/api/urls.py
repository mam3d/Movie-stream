from django.urls import path
from .views import (
    PhoneVerifyCreate,
    RegisterView,
    LoginView
    )

urlpatterns = [
    path("validate-phone/",PhoneVerifyCreate.as_view(),name="validate_phone"),
    path ("register/",RegisterView.as_view(),name="register"),
    path ("login/",LoginView.as_view(),name="login"),
]
