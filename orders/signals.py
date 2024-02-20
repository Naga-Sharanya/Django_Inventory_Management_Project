# orders/signals/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from orders.models import Order
from inventory.models import InventoryMovement

@receiver(post_save, sender=Order)
def update_inventory(sender, instance, **kwargs):
    print(f"Signal triggered for order: {instance.id}")
    print(f"Updating inventory for order: {instance.id}")

    with transaction.atomic():
        print(f"Product quantity before update: {instance.product.quantity}")

        # Calculate the quantity change based on the order quantity
        quantity_change = -instance.quantity

        if instance.product.quantity + quantity_change >= 0:
            instance.product.quantity += quantity_change
            instance.product.save()

            # Create an inventory movement record
            movement_type = 'out of stock'
            InventoryMovement.objects.create(
                product=instance.product,
                supplier=instance.supplier,
                quantity_of_stock=quantity_change,
                movement_type=movement_type
            )

            print(f"Product quantity after update: {instance.product.quantity}")
        else:
            print("Error: Insufficient quantity in stock.")
