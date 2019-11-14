from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'run',
			'nombres',
			'apellidos',
			'correo',
			'nacimiento',
			'telefono',
			'region',
			'ciudad',
			'comuna',
			'vivienda'
			]
