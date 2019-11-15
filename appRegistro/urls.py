from django.urls import path, include
from . import views

urlpatterns = [
	#path('registro', views.registro),
    path('index', views.index),
    path('login', views.usuario_login),
    path('logout', views.usuario_logout),
    path('registro', views.registrar),
]
