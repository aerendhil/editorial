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
	foto = models.ImageField(default='/media/placeholder.png', upload_to='autores/')
	def __str__(self):
		return self.nombre+" "+self.apellido_p+" "+self.apellido_m

class Editorial(models.Model):
	nombre = models.CharField(max_length=50)
	logo = models.ImageField(default='/media/placeholder.png', upload_to='editoriales/')
	def __str__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	fecha_publicacion = models.DateField(auto_now=False, auto_now_add=False)
	portada = models.ImageField(default='/media/placeholder.png', upload_to='libros/')
	precio = models.IntegerField()
	stock = models.IntegerField()
	isbn = models.IntegerField()
	autor = models.ForeignKey('Autor', on_delete='CASCADE')
	editorial = models.ForeignKey('Editorial', on_delete='CASCADE')
	def __str__(self):
		return self.titulo