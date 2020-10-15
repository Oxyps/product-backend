from django.db import models

class Product(models.Model):
	class Meta():
		db_table = 'product'

	def __str__(self):
		return f'{self.nome} R$ {self.preco}'

	nome = models.CharField(unique=True, null=False, max_length=30)
	descricao = models.CharField(null=False, max_length=254)
	preco = models.DecimalField(null=False, max_digits=10, decimal_places=2)
	image_url = models.ImageField(null=False, upload_to='products', max_length=254)