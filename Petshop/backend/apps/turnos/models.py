from django.db import models
from apps.personas.models import Cliente, Peluquero

# Create your models here.
class Turno(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    estaAbonado = models.BooleanField(default=False)
    montoTotal = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)
    peluquero = models.ForeignKey(
        Peluquero,
        on_delete=models.PROTECT,
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
    )