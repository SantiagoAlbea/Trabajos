from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import VentaSerializer, VentaDetalleSerializer, ArticuloSerializer, MetodoDePagoSerializer
from .models import Venta, VentaDetalle, Articulo, MetodoDePago
# Create your views here.

class MetodoDePagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer
    # filterset_class = MetodoDePagoFilter
    ordering_fields = ('nombre',)
    ordering = ('nombre',)

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    # filterset_class = VentaFilter
    ordering_fields = ('fecha',)
    ordering = ('fecha',)
    @action(detail=False)
    def filtro(self, request):
        filtro = Venta.objects.filter(fecha__year='2021', fecha__month='03')
        #fecha__range=["2019-11-08", "2019-11-18"])
        page = self.paginate_queryset(filtro)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(filtro, many=True)
        return Response(serializer.data)

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


