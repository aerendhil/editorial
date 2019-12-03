from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'appRegistro'

urlpatterns = [
    url('index/', views.index, name = 'index'),
    url('login/', views.usuario_login, name = 'login'),
    url('logout/', views.usuario_logout, name = 'logout'),
    url('registro/', views.registrar, name = 'registro'),
    url('gestionEditorial/', views.gestionarEditorial, name = 'gestionEditorial'),
    url('^', include('django.contrib.auth.urls')),
]
