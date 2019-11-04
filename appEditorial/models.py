from django.db import models

# Create your models here.
class Contacto(models.Model):
    correo = models.EmailField()
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    mensaje = models.TextField()
