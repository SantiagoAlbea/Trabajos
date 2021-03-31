from django.contrib import admin

# Register your models here.
from apps.personas.models import (
    Domicilio,
    Cliente,
    Peluquero,
    Proveedor
)

admin.site.register(Domicilio)
admin.site.register(Cliente)
admin.site.register(Peluquero)
admin.site.register(Proveedor)