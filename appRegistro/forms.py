from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import PerfilUsuario


class PerfilUsuarioForm(ModelForm):
    class Meta():
        model = PerfilUsuario
        fields = [
            'run',
            'nacimiento',
            'telefono',
            'region',
            'ciudad',
            'comuna',
            'vivienda'
        ]
        labels = {
            'run': 'RUN',
            'nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Teléfono',
            'region': 'Región',
            'ciudad': 'Ciudad',
            'comuna': 'Comuna',
            'vivienda': 'Vivienda'
        }

    def __init__(self, *args, **kwargs):
        super(PerfilUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['run'].widget.attrs.update({'class': 'form-control'})
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['region'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-control'})
        self.fields['comuna'].widget.attrs.update({'class': 'form-control'})
        self.fields['vivienda'].widget.attrs.update({'class': 'form-control'})


class RegistrarForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido'
        }

    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
