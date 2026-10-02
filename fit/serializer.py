from rest_framework import serializers
from .models import (
    PerfilUsuario,
    Ejercicio,
    PlanEntrenamiento,
    RutinaDetalle,
    ProgresoHistorico,
    AuditoriaEstado
)

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class PlanEntrenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntrenamiento
        fields = '__all__'

class RutinaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaDetalle
        fields = '__all__'

class ProgresoHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoHistorico
        fields = '__all__'

class AuditoriaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaEstado
        fields = '__all__'