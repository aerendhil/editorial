from django.db import models

# Create your models here.
class Contacto(models.Model):
    correo = models.EmailField()
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    mensaje = models.TextField()

class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido_p = models.CharField(max_length=50)
	apellido_m = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
	foto = models.ImageField()

class Editorial(models.Model):
	nombre = models.CharField(max_length=50)
	logo = models.ImageField()

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	fecha_publicacion = models.DateField(auto_now=False, auto_now_add=False)
	precio = models.IntegerField()
	stock = models.IntegerField()
	isbn = models.IntegerField()
	autor = models.ForeignKey('Autor')
	editorial = models.ForeignKey('Editorial')

