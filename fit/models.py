from django.db import models
from django.contrib.auth.models import User

# Variables reutilizables para etiquetas (verbose_name) con prefijos de tipo
int_habilitado = 1
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_observaciones = "Observaciones"

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    nombre_completo = models.CharField("Nombre Completo", max_length=150, null=False)
    rol = models.CharField("Rol", max_length=15, null=False)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Perfil de usuario extendido con rol y datos personales."

    def __str__(self):
        return f"{self.nombre_completo} ({self.rol})"

class Ejercicio(models.Model):
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    descripcion = models.CharField(str_descripcion, max_length=255, null=True)
    grupo_muscular = models.CharField("Grupo Muscular", max_length=50, null=False)
    es_publico = models.BooleanField("Es Público", default=True, null=False)
    creador = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, null=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Catálogo de ejercicios disponibles para confeccionar rutinas."

class PlanEntrenamiento(models.Model):
    cliente = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='planes_asignados', null=False)
    entrenador = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name='planes_dirigidos', null=True)
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    estado = models.CharField("Estado", max_length=15, null=False)
    fecha_inicio = models.DateField("Fecha Inicio", null=False)
    fecha_fin = models.DateField("Fecha Fin", null=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Planes de entrenamiento asignados por entrenadores a clientes."

class RutinaDetalle(models.Model):
    plan = models.ForeignKey(PlanEntrenamiento, on_delete=models.CASCADE, null=False)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, null=False)
    dia_semana = models.IntegerField("Día Semana", null=False)
    series = models.IntegerField("Series", null=False)
    repeticiones = models.IntegerField("Repeticiones", null=False)
    peso_objetivo = models.DecimalField("Peso Objetivo", max_digits=5, decimal_places=2, null=True)
    descanso_segundos = models.IntegerField("Descanso Segundos", null=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Detalle de ejercicios, series y cargas para cada plan."

class ProgresoHistorico(models.Model):
    cliente = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, null=False)
    peso_kg = models.DecimalField("Peso (kg)", max_digits=5, decimal_places=2, null=False)
    porcentaje_grasa = models.DecimalField("Porcentaje Grasa", max_digits=4, decimal_places=2, null=True)
    observaciones = models.CharField(str_observaciones, max_length=255, null=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Historial de mediciones corporales y progresión física del cliente."

class AuditoriaEstado(models.Model):
    plan = models.ForeignKey(PlanEntrenamiento, on_delete=models.CASCADE, null=False)
    estado_anterior = models.CharField("Estado Anterior", max_length=15, null=False)
    estado_nuevo = models.CharField("Estado Nuevo", max_length=15, null=False)
    modificado_por = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, null=True)
    motivo = models.CharField("Motivo", max_length=255, null=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)

    class Meta:
        db_table_comment = "Registro de auditoría sobre cambios de estado en planes de entrenamiento."