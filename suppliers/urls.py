
from django.urls import path
from .views import SupplierAPIView

urlpatterns = [
    path('', SupplierAPIView.as_view(), name='supplier-list-create'),
    path('<int:pk>/', SupplierAPIView.as_view(), name='supplier-detail')

]
