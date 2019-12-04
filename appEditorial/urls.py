from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'appEditorial'

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('', views.home),
	url('home/', views.home, name = 'home'),
	url('catalogo/', views.catalogo, name = 'catalogo'),
    url(r'catalogo$', views.catalogo_filtro, name = 'catalogo_filtro'),
    url(r'editar$', views.editar_libros, name = 'editar_libros'),
    url(r'editar_libro$', views.editar_libro, name = 'editar_libro'),
    url(r'eliminar_libro$', views.eliminar_libro, name = 'eliminar_libro'),
    url('autores/', views.autores, name = 'autores'),
    url('about/', views.about, name = 'about'),
    url('contacto/', views.contacto, name = 'contacto'),
    url('gestionLibros/', views.gestionarLibros, name = 'gestionLibros'),
    url('agregar_libro/', views.agregar_libro, name = 'agregar_libro'),
    url('editar_libro/', views.editar_libro, name = 'editar_libro'),
    url('agregar_autor/', views.agregar_autor, name = 'agregar_autor'),
    url('agregar_editorial/', views.agregar_editorial, name = 'agregar_editorial'),
    path('api/libros/', views.API_libros.as_view()),
    path('api/libros/id/<id>/', views.API_libro_por_id.as_view()),
    path('api/libros/titulo/<titulo>/', views.API_libro_por_titulo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)