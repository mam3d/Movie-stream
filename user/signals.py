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
        subscription,created = Subscription.objects.get_or_create(name="F",price=0)
        UserSubscription.objects.create(user=instance,subscription=subscription)
