from django.db import models
from products.models import Product
from suppliers.models import Supplier
# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()

    def _str_(self):
        return f"Order for {self.product.name} from {self.supplier.brand}"