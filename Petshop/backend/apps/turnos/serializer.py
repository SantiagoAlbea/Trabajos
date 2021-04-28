from rest_framework import serializers
from .models import Turno 
from apps.personas.serializer import ClienteSerializer, PeluqueroSerializer

class TurnoSerializer(serializers.ModelSerializer):
    peluquero = PeluqueroSerializer()
    cliente = ClienteSerializer()
    class Meta:
        model = Turno
        fields = [
            'dia',
            'hora',
            'estaAbonado',
            'montoTotal',
            'observaciones',
            'peso',
            'raza',
            'peluquero',
            'cliente'
        ]