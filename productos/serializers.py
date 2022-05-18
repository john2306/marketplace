from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categoria


class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Producto



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Producto
        depth = 1