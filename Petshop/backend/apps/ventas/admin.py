from django.contrib import admin

# Register your models here.
from apps.ventas.models import (
    Venta,
    Articulo,
    VentaDetalle,
    MetodoDePago
)

admin.site.register(VentaDetalle)
admin.site.register(Articulo)
admin.site.register(Venta)
admin.site.register(MetodoDePago)