from django.forms import ModelForm
from .models import Contacto, Autor, Editorial, Libro

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['correo', 'nombre', 'telefono', 'mensaje']
        labels = {
            'correo': 'Correo',
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
            'mensaje': 'Mensaje'
        }

class LibroForm(ModelForm):
	class Meta:
		model = Libro
		fields = [ 'titulo', 'fecha_publicacion', 'precio', 'stock', 'isbn', 'autor', 'editorial' ]

class AutorForm(ModelForm):
	class Meta:
		model = Autor
		fields = [ 'nombre', 'apellido_p', 'apellido_m', 'fecha_nacimiento', 'foto'  ]

class EditorialForm(ModelForm):
	class Meta:
		model = Editorial
		fields = [ 'nombre', 'logo' ]
