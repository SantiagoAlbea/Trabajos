from rest_framework import serializers
from .models import Venta, VentaDetalle, Articulo

class VentaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venta
        fields = [
            'fecha',
            'hora',
            'montoTotal',
            'cliente',
            'peluquero'
        ]

class ArticuloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Articulo
        fields = [
            'descripcion',
            'precio',
            'stock',
            'proveedor',
        ]

class VentaDetalleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VentaDetalle
        fields = [
            'cantidad',
            'precioUnit',
            'venta',
            'articulo'
        ]
