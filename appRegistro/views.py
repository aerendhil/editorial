from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario
from appEditorial import templates

# Create your views here.
def registro(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit = False)
			model_instance.save()
			return redirect('/editorial')
	else:
		form = UsuarioForm()
		return render(request,
			"appEditorial/registro.html", {'form': form})