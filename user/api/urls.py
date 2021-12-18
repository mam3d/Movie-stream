from django.urls import path
from .views import (
    PhoneVerifyCreate,
    RegisterView,
    LoginView,
    ProfileView,
    SubscriptionView
    )

urlpatterns = [
    path("validate-phone/",PhoneVerifyCreate.as_view(),name="validate_phone"),
    path("register/",RegisterView.as_view(),name="register"),
    path("login/",LoginView.as_view(),name="login"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("subscriptions/",SubscriptionView.as_view(),name="subscriptions"),
]
