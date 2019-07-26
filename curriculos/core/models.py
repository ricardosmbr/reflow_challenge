from django.db import models

# Create your models here.
class Curriculo(models.Model):

	name = models.CharField('Nome',max_length=100)
	description = models.TextField('Desrição',blank=True)
	start_date = models.DateField(
		'Data de Inicio', null=True, blank=True
	)
	image = models.FileField(
		upload_to='images',
		verbose_name='Curriculo',
		null=True,
		blank=True
	)
	create_at = models.DateTimeField(
		'Criando em',auto_now_add=True, null=True, blank=True
	)
	update_at = models.DateTimeField(
		'Atualizado em',auto_now=True, null=True, blank=True
	)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Curriculo'
		verbose_name_plural = 'Curriculos'
		ordering = ['name']

