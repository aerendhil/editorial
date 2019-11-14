from django.shortcuts import render, redirect
from .forms import ContactoForm
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


