from django.contrib import admin
from .models import InventoryMovement
from .models import Supplier
from .models import Product
from .models import Order

admin.site.register(Product)
admin.site.register(InventoryMovement)
admin.site.register(Supplier)
admin.site.register(Order)