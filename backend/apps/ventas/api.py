from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import VentaSerializer, VentaDetalleSerializer, ArticuloSerializer
from .models import Venta, VentaDetalle, Articulo
# Create your views here.

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    # filterset_class = VentaFilter
    ordering_fields = ('fecha',)
    ordering = ('fecha',)

class VentaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalle.objects.all()
    serializer_class = VentaDetalleSerializer
    # filterset_class = VentaDetalleFilter
    ordering_fields = ('cantidad',)
    ordering = ('cantidad',)

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    # filterset_class = ArticuloFilter
    ordering_fields = ('stock',)
    ordering = ('stock',)