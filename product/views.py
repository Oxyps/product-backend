from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import Product, Batch
from .serializers import ProductSerializer, BatchSerializer
from .pagination import CustomPagination

# GET | POST batches
class BatchView(generics.ListCreateAPIView):
	queryset = Batch.objects.all()
	serializer_class = BatchSerializer
	pagination_class = CustomPagination

# GET/:id | PUT | PATCH batches
class BatchDetailView(generics.RetrieveUpdateDestroyAPIView):
# class BatchDetailView(generics.RetrieveUpdateAPIView):
	queryset = Batch.objects.all()
	serializer_class = BatchSerializer
	pagination_class = CustomPagination

# GET | POST products
class ProductView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	pagination_class = CustomPagination

# GET/:id | PUT | DELETE products
class ProductDetailView(APIView):
	def get_object(self, product_id):
		try:
			return Product.objects.get(pk=product_id)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, product_id):
		product = self.get_object(product_id)
		serializer = ProductSerializer(product)
		
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, product_id):
		product = self.get_object(product_id)
		serializer = ProductSerializer(product, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, product_id):
		product = self.get_object(product_id)
		product.delete()
		
		return Response(status=status.HTTP_204_NO_CONTENT)
