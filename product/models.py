from django.db import models

class Product(models.Model):
	class Meta():
		db_table = 'product'

	def __str__(self):
		return f'{self.nome} R$ {self.preco}'

	nome = models.CharField(unique=True, null=False, blank=False, max_length=30)
	descricao = models.CharField(null=False, blank=False, max_length=254)
	preco = models.DecimalField(null=False, blank=False, max_digits=15, decimal_places=2)
	# image_url = models.ImageField(null=False, blank=False, upload_to='products', max_length=254)