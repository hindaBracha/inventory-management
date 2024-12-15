# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from channels.layers import get_channel_layer

@receiver(post_save, sender=Product)
def send_inventory_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    channel_layer.group_send(
        'inventory_updates',
        {
            'type': 'send_inventory_update',
            'message': f"Product {instance.name} stock updated to {instance.stock}"
        }
    )
