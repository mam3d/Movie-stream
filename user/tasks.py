from celery import shared_task
from .models import (
    Subscription,
    UserSubscription
    )


@shared_task(ignore_result=True)
def subscription_expire(user_subscription_id):
    subscription = Subscription.objects.get(name="F")
    user_subscription = UserSubscription.objects.get(id=user_subscription_id)
    user_subscription.date_joined = None
    user_subscription.date_expires = None
    user_subscription.subscription = subscription
    user_subscription.save()
