from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InventoryMovement
from .serializers import InventoryMovementSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import HasModulePermission

class InventoryMovementView(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    def get(self, request, pk=None):
        if pk:
            try:
                movement = InventoryMovement.objects.get(pk=pk)
                serializer = InventoryMovementSerializer(movement)
                return Response(serializer.data)
            except InventoryMovement.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        movements = InventoryMovement.objects.all()
        serializer = InventoryMovementSerializer(movements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryMovementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            movement = InventoryMovement.objects.get(pk=pk)
        except InventoryMovement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InventoryMovementSerializer(movement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movement = InventoryMovement.objects.get(pk=pk)
        except InventoryMovement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)