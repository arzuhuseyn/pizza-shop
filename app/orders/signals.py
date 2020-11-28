from django.db.models import signals
from django.dispatch import receiver

from orders.models import Order, OrderLog


@receiver(signals.post_save, sender=Order, dispatch_uid="order_updated")
def create_order_log(sender, instance, created, **kwargs):
    if not created:
        OrderLog.objects.create(
            order=instance
        )