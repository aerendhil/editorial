from django.forms import ModelForm
from .models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['correo', 'nombre', 'telefono', 'mensaje']
