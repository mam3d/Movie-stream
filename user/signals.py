from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    UserSubscription,
    Subscription,
    CustomUser
    )

@receiver(post_save,sender=CustomUser)
def create_user_subscription(sender,instance,created,**kwargs):
    if created:
        subscription = Subscription.objects.get(name="F")
        UserSubscription.objects.create(user=instance,subscription=subscription)
