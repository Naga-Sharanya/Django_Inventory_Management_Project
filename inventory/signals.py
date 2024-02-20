# inventory/signals/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from orders.models import Order
from inventory.models import InventoryMovement

@receiver(post_save, sender=Order)
def update_inventory(sender, instance, **kwargs):
    print(f"Updating inventory for order: {instance.id}")

    with transaction.atomic():
        print(f"Product quantity before update: {instance.product.quantity}")
        if instance.product.quantity >= instance.quantity:
            instance.product.quantity -= instance.quantity
            instance.product.save()

            # Create an inventory movement record
            InventoryMovement.objects.create(
                product=instance.product,
                supplier=instance.supplier,
                quantity_of_stock=-instance.quantity,
                movement_type='out of stock'
            )

            print(f"Product quantity after update: {instance.product.quantity}")
        else:
            print("Error: Insufficient quantity in stock.")
