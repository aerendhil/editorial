from rest_framework import serializers
from .models import Libro, Editorial, Autor

# Esta clase permite mostrar al autor por su nombre y apellidos
class AutorField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre+" "+value.apellido_p+" "+value.apellido_m

#Clase serializadora para los Libros
class LibroSerializer(serializers.ModelSerializer):
	# Ambas claves foráneas serán mostradas por sus nombres, no sus <id>
	
	# Solicitamos que la editorial se muestre explicitamente por su nombre
	editorial = serializers.ReadOnlyField(source='editorial.nombre')
	# Lo mismo para el autor pero utilizando una clase
	autor= AutorField(read_only=True)

	class Meta:
		model = Libro
		fields = '__all__'