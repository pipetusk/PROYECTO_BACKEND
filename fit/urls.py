from django.urls import path, include
from rest_framework import routers
from fit import views

enrutador = routers.DefaultRouter()

enrutador.register(r'perfiles', views.PerfilUsuarioViewSet)
enrutador.register(r'ejercicios', views.EjercicioViewSet)
enrutador.register(r'planes', views.PlanEntrenamientoViewSet)
enrutador.register(r'rutinas-detalle', views.RutinaDetalleViewSet)
enrutador.register(r'progresos', views.ProgresoHistoricoViewSet)
enrutador.register(r'auditorias', views.AuditoriaEstadoViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]