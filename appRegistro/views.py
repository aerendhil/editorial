from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import PerfilUsuarioForm, RegistrarForm
from .models import PerfilUsuario
from appEditorial import templates

# Create your views here.
def index(request):
	return render(request, "appRegistro/index.html")


def usuario_logout(request):
	if request.user.is_superuser:
		logout(request)
		return HttpResponseRedirect(reverse('appRegistro:login'))
	else:
		logout(request)
		return HttpResponseRedirect(reverse('appEditorial:home'))


def usuario_login(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			return HttpResponseRedirect(reverse('appRegistro:index'))
		else:
			return HttpResponseRedirect(reverse('appEditorial:home'))
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active and user.is_superuser:
					login(request, user)
					return HttpResponseRedirect(reverse('appRegistro:index'))
				elif user.is_active and not user.is_superuser:
					login(request, user)
					return HttpResponseRedirect(reverse('appEditorial:home'))
				else:
					return HttpResponse("Tu cuenta esta inactiva.")
			else:
				return HttpResponse("Datos invalidos.")
		else:
			return render(request, 'appRegistro/login.html')


def registrar(request):
	registrado = False
	if request.method == 'POST':
		user_form = RegistrarForm(data=request.POST)
		profile_form = PerfilUsuarioForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registrado = True
		else:
			return HttpResponse("Datos invalidos.")
	else:
		user_form = RegistrarForm()
		profile_form = PerfilUsuarioForm()

	return render(request, 'appRegistro/registro.html',
					{'user_form': user_form,
					'profile_form': profile_form,
					'registrado': registrado})

