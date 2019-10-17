from django.db import models

# Create your models here.
class Usuario(models.Model):
	run = models.CharField(max_length=20)
	nombres = models.CharField(max_length=50, default = "hola")
	apellidos = models.CharField(max_length=50, default = "hola")
	correo = models.CharField(max_length=50, default = "hola")
	#nacimiento = #DATE
	telefono = models.CharField(max_length=50, default = "hola")
	region = models.CharField(max_length=50, default = "hola")
	ciudad = models.CharField(max_length=50, default = "hola")
	comuna = models.CharField(max_length=50, default = "hola")
	vivienda = models.CharField(max_length=50, default = "hola")