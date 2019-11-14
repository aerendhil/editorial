from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.registro),
    path('listar', views.listar_usuarios),
]
