from django.urls import path, include
from . import views

urlpatterns = [
	path('registro', views.registro),
    path('login', views.login),
    path('listar', views.listar_usuarios),
]
