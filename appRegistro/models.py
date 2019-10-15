from django.db import models

# Create your models here.
class Usuario(models.Model):
	run = models.CharField(max_length=20)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)