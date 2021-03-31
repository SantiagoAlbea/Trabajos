from rest_framework import serializers
from .models import Turno 

class TurnoSerializer(serializers.ModelSerializer):
    
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