from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import HasModulePermission


class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    def get(self, request, pk=None):
        if pk is not None:
            product = Product.objects.filter(pk=pk).first()
            if not product:
                return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ProductSerializer(product)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)