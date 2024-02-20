from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import HasModulePermission

class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    
    def get(self, request, pk=None, format=None):
        # If pk is provided, retrieve a single order, else get all orders
        if pk is not None:
            order = self.get_object(pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
