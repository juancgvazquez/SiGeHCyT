from django.db import models
from django.urls import reverse
import uuid

class Revista(models.Model):
	'''
	Clase para el modelo Revista
	'''
	MESES = (
	('Ene', "Enero"), ("Feb", "Febrero"), ("Mar", "Marzo"), ("Abr", "Abril"), ("May", "Mayo"), ("Jun", "Junio"),
	("Jul", "Julio"), ("Ago", "Agosto"), ("Sep", "Septiembre"), ("Oct", "Octubre"), ("Nov", "Noviembre"),
	("Dic", "Diciembre")
	)
	mes = models.CharField(choices=MESES, max_length=3, verbose_name='Mes', help_text='Ingresar mes de la Revista')
	anio = models.IntegerField()


	def __str__(self):
		return ','.join([self.mes,str(self.anio)])

	def get_absolute_url(self):
		return reverse('DetalleRevistas', args=[str(self.id)])

class Autor(models.Model):
	"""
	Modelo para representar Autor
	"""
	nombre = models.CharField(max_length=100, null=True, blank=True, help_text='Nombre del Autor')
	apellido = models.CharField(max_length=50, help_text='Apellido del Autor')

	class Meta:
		ordering = ['apellido', 'nombre']
		verbose_name_plural = 'Autores'

	def get_absolute_url(self):
		return reverse('DetalleAutores', args=[str(self.id)])

	def __str__(self):
		if self.nombre:
			return '%s, %s' % (self.apellido, self.nombre)
		else:
			return '%s' %(self.apellido)


class Articulo(models.Model):
	'''
	Clase para el modelo Revista
	'''
	#Campos
	titulo = models.CharField(max_length=100, help_text='Título del Artículo')
	revista = models.ForeignKey(Revista, on_delete=models.SET_NULL, null=True, help_text='Revista en la que está el artículo')
	numero = models.IntegerField(help_text='Número de Artículo en la Revista')
	pagina = models.IntegerField(help_text='Página del Artículo')
	autores = models.ManyToManyField(Autor)
	resumen = models.TextField(help_text='Resumen del Artículo')

	#Metadatos
	class Meta:
		ordering = ["titulo"]
		verbose_name = "Artículo"
		verbose_name_plural = "Artículos"

	#Métodos
	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		"""
		Devuelve la URL para la instancia específica de Artículo
		"""
		return reverse('DetalleArtículos', args=[str(self.id)])

	def mostrar_autores(self):
		return ', '.join([autor.apellido for autor in self.autores.all()])

	mostrar_autores.short_description = 'Autores'