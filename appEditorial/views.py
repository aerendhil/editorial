from django.shortcuts import render, redirect
from .forms import ContactoForm, LibroForm
from .models import Contacto


# Create your views here.
def home(request):
	return render(request, 'appEditorial/home.html')

def catalogo(request):
	return render(request, 'appEditorial/catalogo.html')

def autores(request):
    return render(request, 'appEditorial/autores.html')

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

def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit = False)
            model_instance.save()
            message.info(request, 'Libro registrado con éxito')
            return HttpResponseRedirect(reverse('appEditorial:agregar_libro'))
        else:
            message.info(request, 'No se ha podido registrar el libro')
            return HttpResponseRedirect(reverse('appEditorial:agregar_libro'))
    else:
        form = LibroForm()
    return render(request, 'appEditorial/agregarLibro.html',
        {
            'libro_form': form
        })



