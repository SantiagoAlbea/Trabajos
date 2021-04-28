from rest_framework import serializers
from .models import Venta, VentaDetalle, Articulo, MetodoDePago
from apps.personas.serializer import ClienteSerializer, PeluqueroSerializer, ProveedorSerializer

class MetodoDePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoDePago
        fields = [
            'nombre'
        ]

class VentaSerializer(serializers.ModelSerializer):
    peluquero = PeluqueroSerializer()
    cliente = ClienteSerializer()
    metodoDePago = MetodoDePagoSerializer()
    class Meta:
        model = Venta
        fields = [
            'fecha',
            'hora',
            'montoTotal',
            'cliente',
            'peluquero',
            'metodoDePago'
        ]

class ArticuloSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer()
    class Meta:
        model = Articulo
        fields = [
            'descripcion',
            'precio',
            'stock',
            'proveedor',
        ]

class VentaDetalleSerializer(serializers.ModelSerializer):
    venta = VentaSerializer()
    articulo = ArticuloSerializer()
    class Meta:
        model = VentaDetalle
        fields = [
            'cantidad',
            'precioUnit',
            'venta',
            'articulo'
        ]
