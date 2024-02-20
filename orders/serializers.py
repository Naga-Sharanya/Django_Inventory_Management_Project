# # orders/serializers.py
from rest_framework import serializers
from products.models import Product
from suppliers.models import Supplier
from .models import Order



class OrderSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', required=True)
    supplier = serializers.CharField(source='supplier.brand', required=True)

    class Meta:
        model = Order
        fields = ['id', 'quantity', 'product', 'supplier', 'delivery_date']

    def create(self, validated_data):
        product_name = validated_data.pop('product', '')
        supplier_brand = validated_data.pop('supplier', '')

        # Retrieve or create product instance based on the provided name
        product_instance, _ = Product.objects.get_or_create(name=product_name, defaults={'price': 0.0})

        # Retrieve or create supplier instance based on the provided brand
        supplier_instance, _ = Supplier.objects.get_or_create(brand=supplier_brand)

        order = Order.objects.create(
            product=product_instance,
            supplier=supplier_instance,
            **validated_data
        )
        return order
    
    
    def update(self, instance, validated_data):
        product_name = validated_data.pop('product', '')
        supplier_brand = validated_data.pop('supplier', '')

        # Update product instance based on the provided name
        product_instance, _ = Product.objects.get_or_create(name=product_name)
        instance.product = product_instance

        # Update supplier instance based on the provided brand
        supplier_instance, _ = Supplier.objects.get_or_create(brand=supplier_brand)
        instance.supplier = supplier_instance

        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)

        instance.save()
        return instance


