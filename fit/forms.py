from django import forms
from . import models as mod

# --- PERFIL USUARIO ---
class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = mod.PerfilUsuario
        fields = ['usuario', 'nombre_completo', 'rol']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del usuario...',
                'type': 'text'
            }),
            'rol': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Cliente, Entrenador, Admin...',
                'type': 'text'
            }),
        }

class DeshabilitarPerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = mod.PerfilUsuario
        fields = ['habilitado']


# --- EJERCICIO ---
class EjercicioForm(forms.ModelForm):
    class Meta:
        model = mod.Ejercicio
        fields = ['nombre', 'descripcion', 'grupo_muscular', 'es_publico', 'creador']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del ejercicio...',
                'type': 'text'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción o técnica del ejercicio...',
                'rows': '3'
            }),
            'grupo_muscular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Pecho, Espalda, Piernas...',
                'type': 'text'
            }),
            'es_publico': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'creador': forms.Select(attrs={'class': 'form-select'}),
        }

class DeshabilitarEjercicioForm(forms.ModelForm):
    class Meta:
        model = mod.Ejercicio
        fields = ['habilitado']


# --- PLAN ENTRENAMIENTO ---
class PlanEntrenamientoForm(forms.ModelForm):
    class Meta:
        model = mod.PlanEntrenamiento
        fields = ['cliente', 'entrenador', 'nombre', 'estado', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'entrenador': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del plan de entrenamiento...',
                'type': 'text'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Activo, Pausado, Finalizado...',
                'type': 'text'
            }),
            'fecha_inicio': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'fecha_fin': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
        }

class DeshabilitarPlanEntrenamientoForm(forms.ModelForm):
    class Meta:
        model = mod.PlanEntrenamiento
        fields = ['habilitado']


# --- RUTINA DETALLE ---
class RutinaDetalleForm(forms.ModelForm):
    class Meta:
        model = mod.RutinaDetalle
        fields = ['plan', 'ejercicio', 'dia_semana', 'series', 'repeticiones', 'peso_objetivo', 'descanso_segundos']
        widgets = {
            'plan': forms.Select(attrs={'class': 'form-select'}),
            'ejercicio': forms.Select(attrs={'class': 'form-select'}),
            'dia_semana': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Día (1 al 7)...',
                'min': '1',
                'max': '7'
            }),
            'series': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de series...',
                'min': '1'
            }),
            'repeticiones': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Repeticiones por serie...',
                'min': '1'
            }),
            'peso_objetivo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peso en kg (opcional)...',
                'step': '0.5'
            }),
            'descanso_segundos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Segundos de descanso (opcional)...',
                'min': '0'
            }),
        }

class DeshabilitarRutinaDetalleForm(forms.ModelForm):
    class Meta:
        model = mod.RutinaDetalle
        fields = ['habilitado']


# --- PROGRESO HISTÓRICO ---
class ProgresoHistoricoForm(forms.ModelForm):
    class Meta:
        model = mod.ProgresoHistorico
        fields = ['cliente', 'peso_kg', 'porcentaje_grasa', 'observaciones']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'peso_kg': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peso corporal en kg...',
                'step': '0.1'
            }),
            'porcentaje_grasa': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de grasa (opcional)...',
                'step': '0.1'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones del control...',
                'rows': '3'
            }),
        }

class DeshabilitarProgresoHistoricoForm(forms.ModelForm):
    class Meta:
        model = mod.ProgresoHistorico
        fields = ['habilitado']


# --- AUDITORÍA ESTADO ---
class AuditoriaEstadoForm(forms.ModelForm):
    class Meta:
        model = mod.AuditoriaEstado
        fields = ['plan', 'estado_anterior', 'estado_nuevo', 'modificado_por', 'motivo']
        widgets = {
            'plan': forms.Select(attrs={'class': 'form-select'}),
            'estado_anterior': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estado anterior...',
                'type': 'text'
            }),
            'estado_nuevo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estado nuevo...',
                'type': 'text'
            }),
            'modificado_por': forms.Select(attrs={'class': 'form-select'}),
            'motivo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Motivo del cambio de estado...',
                'rows': '3'
            }),
        }