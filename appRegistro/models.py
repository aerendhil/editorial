from django.db import models
import datetime

# Create your models here.
class Usuario(models.Model):
	run = models.CharField(max_length=20, default = "no_asignado")
	nombres = models.CharField(max_length=50, default = "no_asignado")
	apellidos = models.CharField(max_length=50, default = "no_asignado")
	correo = models.EmailField(max_length=254, default = "no_asignado")
	nacimiento = models.DateField(auto_now=False, auto_now_add=False, default= datetime.date(1997, 10, 19))
	telefono = models.CharField(max_length=50, default = "no_asignado")
	region = models.CharField(max_length=50, default = "no_asignado")
	ciudad = models.CharField(max_length=50, default = "no_asignado")
	comuna = models.CharField(max_length=50, default = "no_asignado")
	vivienda = models.CharField(max_length=50, default = "no_asignado")