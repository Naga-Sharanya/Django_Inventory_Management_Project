from django.db import models
from products.models import Product
from suppliers.models import Supplier
from orders.models import Order

class InventoryMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,null=True)
    quantity_of_stock = models.IntegerField()
    MOVEMENT_CHOICES = [
        ('in stock', 'In Stock'),
        ('out of stock', 'Out of Stock'),
        ('return', 'Return'),
        ('adjustment', 'Adjustment'),
    ]
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    movement_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type} of {self.quantity_of_stock} {self.supplier} {self.product.name}"