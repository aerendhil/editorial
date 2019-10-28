from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
	path('home', views.home),
	path('catalogo', views.catalogo),
    path('autores', views.autores),
    path('about', views.about),
]
