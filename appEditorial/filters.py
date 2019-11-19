import django_filters
from .models import Libro

class LibroFilter(django_filters.FilterSet):
	class Meta:
		model = Libro
		fields = [ 'titulo', 'precio', 'autor' ]