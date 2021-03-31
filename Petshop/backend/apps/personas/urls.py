from rest_framework.routers import DefaultRouter
from .api import DomicilioViewSet, ClienteViewSet, ProveedorViewSet, PeluqueroViewSet

app_name = "personas"

router = DefaultRouter()

# url de grupo_permiso
router.register(r'domicilios', DomicilioViewSet, basename='domicilio')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'peluqueros', PeluqueroViewSet, basename='peluqueros')
router.register(r'proveedores', ProveedorViewSet, basename='proveedores')
#router.register(
 #   r'grupo_permisos',
  #  GrupoPermisoViewSet,
  #  basename='grupo_permisos'
#)

#router.register(r'roles', RolViewSet, basename='roles')

urlpatterns = router.urls
