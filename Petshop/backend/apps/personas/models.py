from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    
class Cliente(models.Model):
    codigo = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    mail = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.ForeignKey(
        Domicilio,
        on_delete=models.PROTECT,
    )

class Proveedor(models.Model):
    mail = models.CharField(max_length=50, blank=True, null=True)
    razonSocial = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    telefono2 = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.ForeignKey(
        Domicilio,
        on_delete=models.PROTECT,
    )

class Peluquero(models.Model):
    mail = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.ForeignKey(
        Domicilio,
        on_delete=models.PROTECT,
    )