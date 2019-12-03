from rest_framework import serializers
from .models import Libro

class DRFLibroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Libro
		fields = '__all__'
