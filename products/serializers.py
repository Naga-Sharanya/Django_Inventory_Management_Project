from rest_framework import serializers
from .models import Product
from suppliers.models import Supplier

class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(max_length=100)

    class Meta:
        model = Product
        fields = '__all__'
        
    def get_supplier(self,obj):
        if obj.supplier:
            return obj.supplier.brand

    def create(self, validated_data):
        supplier_data = validated_data.pop('supplier')
        supplier_instance, _ = Supplier.objects.get_or_create(brand=supplier_data)
        product_instance = Product.objects.create(supplier=supplier_instance, **validated_data)
        return product_instance

    def update(self, instance, validated_data):
            supplier_data = validated_data.pop('supplier', None)
            if supplier_data:
                supplier_instance, _ = Supplier.objects.get_or_create(brand=supplier_data)
                instance.supplier = supplier_instance

            instance.name = validated_data.get('name', instance.name)
            instance.price = validated_data.get('price', instance.price)

            instance.save()
            return instance