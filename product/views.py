from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = ProductSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductViewDetail(APIView):
# 	def get(self, request, product_id):
# 		try:
#             product = Product.objects.get(pk=product_id)
#         except Product.DoesNotExist:
#             raise Http404
        
# 		serializer = serializers.ProductSerializer(data=product)
#         return Response(serializer.data)

	# def update(self, request):

	# def delete(self, request, product_id):
	#     try:
	#         restaurant = Restaurant.objects.get(pk=restaurant_id)
	#     except Restaurant.DoesNotExist:
	#         raise Http404
	#     restaurant.delete()
	#     return Response(status=status.HTTP_204_NO_CONTENT)

