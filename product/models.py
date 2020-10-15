from django.db import models

class Product(models.Model):
	class Meta():
		db_table = 'product'

	def __str__(self):
		return f'{self.name} R$ {self.price}'

	name = models.CharField(unique=True, null=False, max_length=30)
	description = models.CharField(null=False, max_length=254)
	price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
	image = models.ImageField(null=False, upload_to='products', max_length=254)