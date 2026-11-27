from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class PlanEntrenamientoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PlanEntrenamiento.objects.all()
    serializer_class = PlanEntrenamientoSerializer

class RutinaDetalleViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = RutinaDetalle.objects.all()
    serializer_class = RutinaDetalleSerializer

class ProgresoHistoricoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProgresoHistorico.objects.all()
    serializer_class = ProgresoHistoricoSerializer

class AuditoriaEstadoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = AuditoriaEstado.objects.all()
    serializer_class = AuditoriaEstadoSerializer


# ==========================================
# 2. VISTAS BASADAS EN CLASES (CRUD WEB)
# ==========================================

# -- INICIO (VISTA PÚBLICA) --
class IndexView(TemplateView):
    template_name = 'fit/index.html'

# -- AUDITORÍA --
class AuditoriaListView(LoginRequiredMixin, ListView):
    model = AuditoriaEstado
    template_name = 'fit/auditoria/listado_auditorias.html'

# -- EJERCICIOS --
class EjercicioListView(LoginRequiredMixin, ListView):
    model = Ejercicio
    template_name = 'fit/ejercicio/listado_ejercicios.html'

class EjercicioCreateView(LoginRequiredMixin, CreateView):
    model = Ejercicio
    form_class = forms.EjercicioForm
    success_url = reverse_lazy('listado_ejercicios')
    template_name = 'fit/ejercicio/crear_ejercicio.html'

class EjercicioUpdateView(LoginRequiredMixin, UpdateView):
    model = Ejercicio
    form_class = forms.EjercicioForm
    success_url = reverse_lazy('listado_ejercicios')
    template_name = 'fit/ejercicio/crear_ejercicio.html'

class EjercicioDetailView(LoginRequiredMixin, DetailView):
    model = Ejercicio
    template_name = 'fit/ejercicio/detalle_ejercicio.html'

class EjercicioDeshabilitarView(LoginRequiredMixin, UpdateView):
    model = Ejercicio
    form_class = forms.DeshabilitarEjercicioForm
    success_url = reverse_lazy('listado_ejercicios')
    template_name = 'fit/ejercicio/eliminar_ejercicio.html'

    def form_valid(self, form):
        form.instance.habilitado = False
        return super().form_valid(form)

# -- PERFILES --
class PerfilListView(LoginRequiredMixin, ListView):
    model = PerfilUsuario
    template_name = 'fit/perfil/listado_perfiles.html'

class PerfilCreateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    form_class = forms.PerfilForm
    success_url = reverse_lazy('listado_perfiles')
    template_name = 'fit/perfil/crear_perfil.html'

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario
    form_class = forms.PerfilForm
    success_url = reverse_lazy('listado_perfiles')
    template_name = 'fit/perfil/crear_perfil.html'

class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = PerfilUsuario
    template_name = 'fit/perfil/detalle_perfil.html'

class PerfilDeshabilitarView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario
    form_class = forms.DeshabilitarPerfilForm
    success_url = reverse_lazy('listado_perfiles')
    template_name = 'fit/perfil/eliminar_perfil.html'

    def form_valid(self, form):
        form.instance.habilitado = False
        return super().form_valid(form)

# -- PLANES DE ENTRENAMIENTO --
class PlanListView(LoginRequiredMixin, ListView):
    model = PlanEntrenamiento
    template_name = 'fit/plan/listado_planes.html'

class PlanCreateView(LoginRequiredMixin, CreateView):
    model = PlanEntrenamiento
    form_class = forms.PlanForm
    success_url = reverse_lazy('listado_planes')
    template_name = 'fit/plan/crear_plan.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        AuditoriaEstado.objects.create(
            plan=self.object,
            estado_anterior='Nuevo',
            estado_nuevo=self.object.estado,
            modificado_por=self.object.entrenador or self.object.cliente,
            motivo='Creación inicial del plan de entrenamiento.'
        )
        return response

class PlanUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanEntrenamiento
    form_class = forms.PlanForm
    success_url = reverse_lazy('listado_planes')
    template_name = 'fit/plan/crear_plan.html'

    def form_valid(self, form):
        estado_previo = PlanEntrenamiento.objects.get(pk=self.object.pk).estado
        response = super().form_valid(form)
        AuditoriaEstado.objects.create(
            plan=self.object,
            estado_anterior=estado_previo,
            estado_nuevo=self.object.estado,
            modificado_por=self.object.entrenador or self.object.cliente,
            motivo='Actualización del plan de entrenamiento.'
        )
        return response

class PlanDetailView(LoginRequiredMixin, DetailView):
    model = PlanEntrenamiento
    template_name = 'fit/plan/detalle_plan.html'

class PlanDeshabilitarView(LoginRequiredMixin, UpdateView):
    model = PlanEntrenamiento
    form_class = forms.DeshabilitarPlanForm
    success_url = reverse_lazy('listado_planes')
    template_name = 'fit/plan/eliminar_plan.html'

    def form_valid(self, form):
        estado_previo = PlanEntrenamiento.objects.get(pk=self.object.pk).estado
        form.instance.habilitado = False
        form.instance.estado = 'Deshabilitado'
        response = super().form_valid(form)
        AuditoriaEstado.objects.create(
            plan=self.object,
            estado_anterior=estado_previo,
            estado_nuevo='Deshabilitado',
            modificado_por=self.object.entrenador or self.object.cliente,
            motivo='Deshabilitación lógica del plan de entrenamiento.'
        )
        return response

# -- RUTINAS --
class RutinaListView(LoginRequiredMixin, ListView):
    model = RutinaDetalle
    template_name = 'fit/rutina/listado_rutinas.html'

class RutinaCreateView(LoginRequiredMixin, CreateView):
    model = RutinaDetalle
    form_class = forms.RutinaForm
    success_url = reverse_lazy('listado_rutinas')
    template_name = 'fit/rutina/crear_rutina.html'

class RutinaUpdateView(LoginRequiredMixin, UpdateView):
    model = RutinaDetalle
    form_class = forms.RutinaForm
    success_url = reverse_lazy('listado_rutinas')
    template_name = 'fit/rutina/crear_rutina.html'

class RutinaDetailView(LoginRequiredMixin, DetailView):
    model = RutinaDetalle
    template_name = 'fit/rutina/detalle_rutina.html'

class RutinaDeshabilitarView(LoginRequiredMixin, UpdateView):
    model = RutinaDetalle
    form_class = forms.DeshabilitarRutinaForm
    success_url = reverse_lazy('listado_rutinas')
    template_name = 'fit/rutina/eliminar_rutina.html'

    def form_valid(self, form):
        form.instance.habilitado = False
        return super().form_valid(form)

# -- PROGRESOS --
class ProgresoListView(LoginRequiredMixin, ListView):
    model = ProgresoHistorico
    template_name = 'fit/progreso/listado_progresos.html'

class ProgresoCreateView(LoginRequiredMixin, CreateView):
    model = ProgresoHistorico
    form_class = forms.ProgresoForm
    success_url = reverse_lazy('listado_progresos')
    template_name = 'fit/progreso/crear_progreso.html'

class ProgresoUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgresoHistorico
    form_class = forms.ProgresoForm
    success_url = reverse_lazy('listado_progresos')
    template_name = 'fit/progreso/crear_progreso.html'

class ProgresoDetailView(LoginRequiredMixin, DetailView):
    model = ProgresoHistorico
    template_name = 'fit/progreso/detalle_progreso.html'

class ProgresoDeshabilitarView(LoginRequiredMixin, UpdateView):
    model = ProgresoHistorico
    form_class = forms.DeshabilitarProgresoForm
    success_url = reverse_lazy('listado_progresos')
    template_name = 'fit/progreso/eliminar_progreso.html'

    def form_valid(self, form):
        form.instance.habilitado = False
        return super().form_valid(form)


# ==========================================
# 3. VISTAS DE AUTENTICACIÓN Y REGISTRO (FBV)
# ==========================================
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['mensaje_bienvenida'] = '¡Bienvenido!'
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
