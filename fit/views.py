from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    PerfilUsuario, 
    Ejercicio, 
    PlanEntrenamiento, 
    RutinaDetalle, 
    ProgresoHistorico, 
    AuditoriaEstado
)

from .serializer import (
    PerfilUsuarioSerializer, 
    EjercicioSerializer, 
    PlanEntrenamientoSerializer, 
    RutinaDetalleSerializer, 
    ProgresoHistoricoSerializer, 
    AuditoriaEstadoSerializer
)

# Create your views here.
def home(request):
    return render(request, 'fit/index.html')

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class PlanEntrenamientoViewSet(viewsets.ModelViewSet):
    queryset = PlanEntrenamiento.objects.all()
    serializer_class = PlanEntrenamientoSerializer

class RutinaDetalleViewSet(viewsets.ModelViewSet):
    queryset = RutinaDetalle.objects.all()
    serializer_class = RutinaDetalleSerializer

class ProgresoHistoricoViewSet(viewsets.ModelViewSet):
    queryset = ProgresoHistorico.objects.all()
    serializer_class = ProgresoHistoricoSerializer

class AuditoriaEstadoViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaEstado.objects.all()
    serializer_class = AuditoriaEstadoSerializer