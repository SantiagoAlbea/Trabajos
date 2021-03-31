from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import DomicilioSerializer, ClienteSerializer, PeluqueroSerializer, ProveedorSerializer
from .models import Domicilio, Cliente, Proveedor, Peluquero
# Create your views here.

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer
    # filterset_class = DomicilioFilter
    ordering_fields = ('calle',)
    ordering = ('calle',)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # filterset_class = ClienteFilter
    ordering_fields = ('dni',)
    ordering = ('dni',)

class PeluqueroViewSet(viewsets.ModelViewSet):
    queryset = Peluquero.objects.all()
    serializer_class = PeluqueroSerializer
    # filterset_class = PeluqueroFilter
    ordering_fields = ('nombre',)
    ordering = ('nombre',)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    # filterset_class = ProveedorFilter
    ordering_fields = ('razonSocial',)
    ordering = ('razonSocial',)