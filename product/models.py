from django.db import models

from .choices import SIZE_CHOICES

class Batch(models.Model):
	class Meta():
		db_table = 'batch'

	def __str__(self):
		return f'{self.code}'

	code = models.CharField(null=False, blank=False, unique=True, max_length=50)
	producer = models.CharField(null=False, blank=False, max_length=20)
	produce_date = models.DateField(null=False, blank=False)
	shelf_life = models.DateField(null=False, blank=False)
	size = models.CharField(null=False, blank=False, choices=SIZE_CHOICES, max_length=1, default='M')

class Product(models.Model):
	class Meta():
		db_table = 'product'

	def __str__(self):
		return f'{self.nome} ({self.batch.size}) R$ {self.preco}'

	nome = models.CharField(unique=True, null=False, blank=False, max_length=30)
	descricao = models.CharField(null=False, blank=False, max_length=254)
	preco = models.DecimalField(null=False, blank=False, max_digits=15, decimal_places=2)
	
	batch = models.ForeignKey('Batch', db_column='batch_id', on_delete=models.PROTECT)

	# image_url = models.ImageField(null=False, blank=False, upload_to='products', max_length=254)