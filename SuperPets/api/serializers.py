from .models import Producto
from rest_framework import serializers

""" Ahora vamos a configurar un serializador, éste definirá el contenido de las películas tal 
    como las devolverá la API: """


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
