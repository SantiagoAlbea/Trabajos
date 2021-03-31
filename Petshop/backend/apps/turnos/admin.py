from django.contrib import admin

# Register your models here.
from apps.turnos.models import (
    Turno
)

admin.site.register(Turno)