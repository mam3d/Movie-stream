from rest_framework.permissions import BasePermission
from ..models import UserSubscription

class SubscriptionPermission(BasePermission):
    message = "You have to purchase pro subscription in order to view this page"
    def has_permission(self, request, view):
        user = request.user
        user_subscription = UserSubscription.objects.get(user__phone=user)
        return bool(user_subscription.subscription.name == "P")
        