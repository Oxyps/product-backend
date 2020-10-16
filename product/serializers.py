from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = '__all__'

	def get_image_url(self, product):
		request = self.context.get('request')
		image_url = product.image_url.url
		return request.build_absolute_uri(image_url)

	def create(self, validated_data):
		return Product.objects.create(**validated_data)