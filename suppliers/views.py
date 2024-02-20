from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import HasModulePermission


class SupplierAPIView(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    serializer_class = SupplierSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            supplier = self.get_object(pk)
            serializer = self.serializer_class(supplier)
        else:
            suppliers = Supplier.objects.all()
            serializer = self.serializer_class(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
            supplier = get_object_or_404(Supplier, pk=pk)
            serializer = self.serializer_class(supplier, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise Http404
