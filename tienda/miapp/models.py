from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class articulos(models.Model):
	tipo = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	precio = models.CharField(max_length=10)
	foto = models.ImageField(upload_to='miapp/static/media')
	def __str__(self):
		return '%s' % (self.nombre)

class item(models.Model):
	talla = models.CharField(max_length=2)
	color = models.CharField(max_length=20)
	articulos = models.ForeignKey(articulos)
	def __str__(self):
		return '%s' % (self.talla)

class comentarios(models.Model):
	comentario = models.CharField(max_length=100)
	articulos = models.ForeignKey(articulos,null=True)
	usuario = models.ForeignKey (User,null=True)
