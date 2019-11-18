from django.db import models
from django.contrib.auth.models import User
import datetime


class PerfilUsuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	run = models.CharField(max_length=20)
	nacimiento = models.DateField(auto_now=False, auto_now_add=False)
	telefono = models.CharField(max_length=50)
	region = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	comuna = models.CharField(max_length=50)
	vivienda = models.CharField(max_length=50)

	def __str__(self):
		return self.run

