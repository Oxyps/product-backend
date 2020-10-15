from django.urls import path

from .views import ProductView, ProductViewDetail

urlpatterns = [
	path('products/', ProductView.as_view(), name='products'),
	path('products/<int:product_id>/', ProductViewDetail.as_view(), name='product-detail'),
]