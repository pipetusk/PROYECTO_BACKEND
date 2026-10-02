from django.contrib import admin

# Register your models here.
from .models import (
    PerfilUsuario,
    Ejercicio,
    PlanEntrenamiento,
    RutinaDetalle,
    ProgresoHistorico,
    AuditoriaEstado
)

# Registramos todos los modelos para que aparezcan en el panel de administración
admin.site.register(PerfilUsuario)
admin.site.register(Ejercicio)
admin.site.register(PlanEntrenamiento)
admin.site.register(RutinaDetalle)
admin.site.register(ProgresoHistorico)
admin.site.register(AuditoriaEstado)