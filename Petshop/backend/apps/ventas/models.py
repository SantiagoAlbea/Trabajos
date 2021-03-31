from django.db import models
from apps.personas.models import Proveedor, Cliente, Peluquero

# Create your models here.
class Articulo(models.Model):
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
    )

class Venta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    montoTotal = models.FloatField()
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
    )
    peluquero = models.ForeignKey(
        Peluquero,
        on_delete=models.PROTECT,
        blank=True, 
        null=True,
    )

class VentaDetalle(models.Model):
    cantidad = models.IntegerField()
    precioUnit = models.FloatField()
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
    )
    articulo = models.ForeignKey(
        Articulo,
        on_delete=models.CASCADE,
    )