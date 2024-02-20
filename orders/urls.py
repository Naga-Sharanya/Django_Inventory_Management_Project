from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('', OrderAPIView.as_view(), name='orders-list'),  
    path('<int:pk>/', OrderAPIView.as_view(), name='orders-detail'),  
]