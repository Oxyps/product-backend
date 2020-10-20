from django.urls import path

from .views import ProductView, BatchView, ProductDetailView, BatchDetailView

urlpatterns = [
	path('products/', ProductView.as_view(), name='products'),
	path('products/<int:product_id>/', ProductDetailView.as_view(), name='product-detail'),
	path('batches/', BatchView.as_view(), name='batches'),
	path('batches/<int:pk>/', BatchDetailView.as_view(), name='batch-detail'),
]