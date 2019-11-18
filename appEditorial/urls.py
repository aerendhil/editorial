from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'appEditorial'

urlpatterns = [
    path('', views.home),
	url('home/', views.home, name = 'home'),
	url('catalogo/', views.catalogo, name = 'catalogo'),
    url('autores/', views.autores, name = 'autores'),
    url('about/', views.about, name = 'about'),
    url('contacto/', views.contacto, name = 'contacto'),
    url('agregar_libro/', views.agregar_libro, name = 'agregar_libro'),
    url('agregar_autor/', views.agregar_autor, name = 'agregar_autor'),
    url('agregar_editorial/', views.agregar_editorial, name = 'agregar_editorial'),
]
