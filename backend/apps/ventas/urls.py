from rest_framework.routers import DefaultRouter
from .api import VentaViewSet, VentaDetalleViewSet, ArticuloViewSet
from django.urls import path

app_name = "ventas"

router = DefaultRouter()

router.register(r'ventas', VentaViewSet)
router.register(r'ventadetalles', VentaDetalleViewSet)
router.register(r'articulos', ArticuloViewSet)

urlpatterns = router.urls

#urlpatterns += [
    #path('admin/', admin.site.urls)
    #path('ventas/', VentaViewSet, name='ventas'),
    #path('ventadetalles/', VentaDetalleViewSet, name='ventadetalles'),
    #path('articulos/', ArticuloViewSet, name='articulos'),
#]

#urlpatterns += router.urls
