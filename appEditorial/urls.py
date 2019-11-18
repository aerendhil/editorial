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
]
