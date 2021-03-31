from rest_framework.routers import DefaultRouter
from .api import TurnoViewSet

app_name = "turnos"

router = DefaultRouter()

# url de grupo_permiso
router.register(r'turnos', TurnoViewSet, basename='turnos')

#router.register(
 #   r'grupo_permisos',
  #  GrupoPermisoViewSet,
  #  basename='grupo_permisos'
#)

#router.register(r'roles', RolViewSet, basename='roles')

urlpatterns = []

urlpatterns += router.urls