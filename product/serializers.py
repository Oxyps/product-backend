from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	image_url = serializers.ImageField(
		# null=False,
		max_length=254,
		use_url=True
	)

	class Meta:
		model = Product
		fields = '__all__'

	def create(self, validated_data):
		return Product.objects.create(**validated_data)