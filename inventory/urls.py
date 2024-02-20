from django.urls import path
from .views import InventoryMovementView

urlpatterns = [
    path('', InventoryMovementView.as_view(), name='inventory-list'),  
    path('<int:pk>/', InventoryMovementView.as_view(), name='inventory-detail'),  
]