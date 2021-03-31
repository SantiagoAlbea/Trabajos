from rest_framework import serializers
from .models import Domicilio, Cliente, Peluquero, Proveedor 

class DomicilioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Domicilio
        fields = [
            'calle',
            'numero',
            'localidad'
        ]

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = [
            'codigo',
            'dni',
            'mail',
            'nombre',
            'apellido',
            'telefono',
            'domicilio'
        ]

class PeluqueroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Peluquero
        fields = [
            'mail',
            'nombre',
            'telefono',
            'domicilio'
        ]

class ProveedorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proveedor
        fields = [
            'mail',
            'razonSocial',
            'telefono',
            'telefono2',
            'domicilio'
        ]