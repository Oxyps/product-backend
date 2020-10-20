from rest_framework import serializers

from .models import Product, Batch
from .choices import SIZE_CHOICES

class BatchSerializer(serializers.ModelSerializer):
	size = serializers.ChoiceField(choices=SIZE_CHOICES)

	class Meta:
		model = Batch
		fields = '__all__'

	def create(self, validated_data):
		return Batch.objects.create(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

	def create(self, validated_data):
		return Product.objects.create(**validated_data)