from django.shortcuts import render, redirect

# Create your views here.
def registro(request):
	if request.method == "POST":
		form = CarreraForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit = false)
			model_instance.save()
			return redirect('registo_completado')