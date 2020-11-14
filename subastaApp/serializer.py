
"""
from rest_framework import serializers
from .model import Vehiculo
from rest_framework.serializer import ModelSerializer

class VehiculoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
"""