from rest_framework import serializers
from products.models import Product
from suppliers.models import Supplier
from .models import InventoryMovement

class InventoryMovementSerializer(serializers.ModelSerializer):
    product = serializers.CharField(max_length=100)
    supplier = serializers.CharField(max_length=100)

    class Meta:
        model = InventoryMovement
        fields = ('id', 'product', 'supplier', 'quantity_of_stock', 'movement_type', 'movement_date')

    def create(self, validated_data):
        # Retrieve or create the Product instance based on the provided name
        product_name = validated_data.pop('product', '')
        product_instance, _ = Product.objects.get_or_create(name=product_name, price=0)  # Provide a default price value

        # Retrieve or create the Supplier instance based on the provided name
        supplier_name = validated_data.pop('supplier', '')
        supplier_instance, _ = Supplier.objects.get_or_create(brand=supplier_name)

        validated_data['product'] = product_instance
        validated_data['supplier'] = supplier_instance

        return InventoryMovement.objects.create(**validated_data)

    def update(self, instance, validated_data):
    # Retrieve or create the Product instance based on the provided name
        product_name = validated_data.pop('product', instance.product.name)
        product_instance, _ = Product.objects.get_or_create(name=product_name)

        # Retrieve or create the Supplier instance based on the provided name
        supplier_name = validated_data.pop('supplier', instance.supplier.brand)
        supplier_instance, _ = Supplier.objects.get_or_create(brand=supplier_name)

        instance.product = product_instance
        instance.supplier = supplier_instance
        instance.quantity_of_stock = validated_data.get('quantity_of_stock', instance.quantity_of_stock)
        instance.movement_type = validated_data.get('movement_type', instance.movement_type)
        instance.movement_date = validated_data.get('movement_date', instance.movement_date)  # Provide a default value if not provided
        instance.save()
        return instance

