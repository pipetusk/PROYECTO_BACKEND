from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from rest_framework import viewsets

# Importamos los modelos y serializadores de tu app
from .models import (
    PerfilUsuario, Ejercicio, PlanEntrenamiento, 
    RutinaDetalle, ProgresoHistorico, AuditoriaEstado
)
from .serializers import (
    PerfilUsuarioSerializer, EjercicioSerializer, PlanEntrenamientoSerializer, 
    RutinaDetalleSerializer, ProgresoHistoricoSerializer, AuditoriaEstadoSerializer
)

# Importamos los formularios (asumiendo que los crearás en forms.py)
from . import forms

# ==========================================
# 1. VISTAS DE LA API REST (ViewSets)
# ==========================================
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


# ==========================================
# 2. VISTAS BASADAS EN CLASES (CRUD WEB)
# ==========================================

# -- INICIO --
class IndexView(TemplateView):
    template_name = 'fit/index.html'

# -- AUDITORÍA --
class AuditoriaListView(ListView):
    model = AuditoriaEstado
    template_name = 'fit/auditoria/listado_auditorias.html'

# -- EJERCICIOS --
class EjercicioListView(ListView):
    model = Ejercicio
    template_name = 'fit/ejercicio/listado_ejercicios.html'

class EjercicioCreateView(CreateView):
    model = Ejercicio
    form_class = forms.EjercicioForm
    success_url = reverse_lazy('listado_ejercicios')
    template_name = 'fit/ejercicio/crear_ejercicio.html'

class EjercicioUpdateView(UpdateView):
    model = Ejercicio
    form_class = forms.EjercicioForm
    success_url = reverse_lazy('listado_ejercicios')
    template_name = 'fit/ejercicio/crear_ejercicio.html'

class EjercicioDetailView(DetailView):
    model = Ejercicio
    template_name = 'fit/ejercicio/detalle_ejercicio.html'

class EjercicioDeshabilitarView(UpdateView):
    model = Ejercicio
    form_class = forms.DeshabilitarEjercicioForm
    success_url = reverse_lazy('listado_ejercicios')
    template_name = 'fit/ejercicio/eliminar_ejercicio.html'

# -- PERFILES --
class PerfilListView(ListView):
    model = PerfilUsuario
    template_name = 'fit/perfil/listado_perfiles.html'

class PerfilCreateView(CreateView):
    model = PerfilUsuario
    form_class = forms.PerfilForm
    success_url = reverse_lazy('listado_perfiles')
    template_name = 'fit/perfil/crear_perfil.html'

class PerfilUpdateView(UpdateView):
    model = PerfilUsuario
    form_class = forms.PerfilForm
    success_url = reverse_lazy('listado_perfiles')
    template_name = 'fit/perfil/crear_perfil.html'

class PerfilDetailView(DetailView):
    model = PerfilUsuario
    template_name = 'fit/perfil/detalle_perfil.html'

class PerfilDeshabilitarView(UpdateView):
    model = PerfilUsuario
    form_class = forms.DeshabilitarPerfilForm
    success_url = reverse_lazy('listado_perfiles')
    template_name = 'fit/perfil/eliminar_perfil.html'

# -- PLANES DE ENTRENAMIENTO --
class PlanListView(ListView):
    model = PlanEntrenamiento
    template_name = 'fit/plan/listado_planes.html'

class PlanCreateView(CreateView):
    model = PlanEntrenamiento
    form_class = forms.PlanForm
    success_url = reverse_lazy('listado_planes')
    template_name = 'fit/plan/crear_plan.html'

class PlanUpdateView(UpdateView):
    model = PlanEntrenamiento
    form_class = forms.PlanForm
    success_url = reverse_lazy('listado_planes')
    template_name = 'fit/plan/crear_plan.html'

class PlanDetailView(DetailView):
    model = PlanEntrenamiento
    template_name = 'fit/plan/detalle_plan.html'

class PlanDeshabilitarView(UpdateView):
    model = PlanEntrenamiento
    form_class = forms.DeshabilitarPlanForm
    success_url = reverse_lazy('listado_planes')
    template_name = 'fit/plan/eliminar_plan.html'

# -- RUTINAS --
class RutinaListView(ListView):
    model = RutinaDetalle
    template_name = 'fit/rutina/listado_rutinas.html'

class RutinaCreateView(CreateView):
    model = RutinaDetalle
    form_class = forms.RutinaForm
    success_url = reverse_lazy('listado_rutinas')
    template_name = 'fit/rutina/crear_rutina.html'

class RutinaUpdateView(UpdateView):
    model = RutinaDetalle
    form_class = forms.RutinaForm
    success_url = reverse_lazy('listado_rutinas')
    template_name = 'fit/rutina/crear_rutina.html'

class RutinaDetailView(DetailView):
    model = RutinaDetalle
    template_name = 'fit/rutina/detalle_rutina.html'

class RutinaDeshabilitarView(UpdateView):
    model = RutinaDetalle
    form_class = forms.DeshabilitarRutinaForm
    success_url = reverse_lazy('listado_rutinas')
    template_name = 'fit/rutina/eliminar_rutina.html'

# -- PROGRESOS --
class ProgresoListView(ListView):
    model = ProgresoHistorico
    template_name = 'fit/progreso/listado_progresos.html'

class ProgresoCreateView(CreateView):
    model = ProgresoHistorico
    form_class = forms.ProgresoForm
    success_url = reverse_lazy('listado_progresos')
    template_name = 'fit/progreso/crear_progreso.html'

class ProgresoUpdateView(UpdateView):
    model = ProgresoHistorico
    form_class = forms.ProgresoForm
    success_url = reverse_lazy('listado_progresos')
    template_name = 'fit/progreso/crear_progreso.html'

class ProgresoDetailView(DetailView):
    model = ProgresoHistorico
    template_name = 'fit/progreso/detalle_progreso.html'

class ProgresoDeshabilitarView(UpdateView):
    model = ProgresoHistorico
    form_class = forms.DeshabilitarProgresoForm
    success_url = reverse_lazy('listado_progresos')
    template_name = 'fit/progreso/eliminar_progreso.html'