from django.shortcuts import render, redirect


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
    return render(request, 'appEditorial/contacto.html')
