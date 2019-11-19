import django_filters
from django.db import models

from .models import Libro

class LibroFilter(django_filters.FilterSet):

	class Meta:
		model = Libro
		fields = [ 'titulo', 'precio', 'autor' ]
		filter_overrides = {
			models.CharField: {
				'filter_class': django_filters.CharFilter,
				'extra': lambda f: {
					'lookup_expr': 'icontains'
				}
			}
		}