from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from rest_framework import generics

from .forms import ContactoForm, LibroForm, AutorForm, EditorialForm
from .models import Contacto, Libro, Autor
from .filters import LibroFilter
from .serializers import DRFLibroSerializer

# Create your views here.
def home(request):
	return render(request, 'appEditorial/home.html')

def catalogo(request):
    catalogo = Libro.objects.all()
    filtros = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(
        request, 'appEditorial/catalogo.html', {'catalogo': catalogo}, {'filtros': filtros}
        )
def catalogo_filtro(request):
    filtro = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(
        request, 'appEditorial/catalogo.html', {'filtros': filtro}
        )

def editar_libros(request):
    filtro = LibroFilter(request.GET, queryset=Libro.objects.all())
    return render(
        request, 'appEditorial/seleccionar_libros.html', {'filtros': filtro}
        )

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'appEditorial/autores.html', {'autores': autores})

def about(request):
    return render(request, 'appEditorial/about.html')

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            return redirect('/editorial/contacto')
    else:
        form = ContactoForm()
        return render(request,
            "appEditorial/contacto.html", {'form': form})


def gestionarLibros(request):
    return render(request, 'appEditorial/gestionarLibros.html')


def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            messages.info(request, 'Libro registrado con éxito')
            return HttpResponseRedirect(reverse('appEditorial:agregar_libro'))
        else:
            messages.info(request, 'No se ha podido registrar el libro')
            return HttpResponseRedirect(reverse('appEditorial:agregar_libro'))
    else:
        form = LibroForm()
    return render(request, 'appEditorial/agregarLibro.html',
        {
            'libro_form': form,
        })


def editar_libro(request):
    libro_id = request.GET['id']
    libro = Libro.objects.get(id=libro_id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            return HttpResponseRedirect(reverse('appEditorial:editar_libros'))
        else:
            return HttpResponseRedirect(reverse('appEditorial:editar_libros'))
    else:
        form = LibroForm(instance=libro)
        return render(request, 'appEditorial/editar_libro.html',
            {
                'libro_form': form,
            })

def eliminar_libro(request):
    libro_id = request.GET['id']
    libro = Libro.objects.get(id=libro_id)
    libro.delete()
    messages.info(request, 'Libro eliminado correctamente')
    return HttpResponseRedirect(reverse('appEditorial:editar_libros'))

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            messages.info(request, 'Autor registrado con éxito')
            return HttpResponseRedirect(reverse('appEditorial:agregar_autor'))
        else:
            messages.info(request, 'No se ha podido registrar el autor')
            return HttpResponseRedirect(reverse('appEditorial:agregar_autor'))
    else:
        form = AutorForm()
    return render(request, 'appEditorial/agregarAutor.html',
        {
            'autor_form': form
        })

def agregar_editorial(request):
    if request.method == "POST":
        form = EditorialForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            messages.info(request, 'Editorial registrada con éxito')
            return HttpResponseRedirect(reverse('appEditorial:agregar_editorial'))
        else:
            messages.info(request, 'No se ha podido registrar la editorial')
            return HttpResponseRedirect(reverse('appEditorial:agregar_editorial'))
    else:
        form = EditorialForm()
    return render(request, 'appEditorial/agregarEditorial.html',
        {
            'editorial_form': form
        })

class API_libros(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = DRFLibroSerializer

class API_libros_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = DRFLibroSerializer
