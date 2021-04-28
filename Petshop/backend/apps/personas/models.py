from django.db import models

#from django.conf import settings
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from rest_framework.authtoken.models import Token

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)
        
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

