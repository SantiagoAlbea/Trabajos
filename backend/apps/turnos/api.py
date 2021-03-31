from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import TurnoSerializer
from .models import Turno
# Create your views here.

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    # filterset_class = TurnoFilter
    ordering_fields = ('dia',)
    ordering = ('dia',)

