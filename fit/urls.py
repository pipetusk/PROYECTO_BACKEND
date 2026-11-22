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
    # 1. API REST (ViewSets generados por ti inicialmente)
    path('', include(enrutador.urls)),
    
    # 2. Ruta de Inicio (Index de la web)
    path('inicio/', views.IndexView.as_view(), name='inicio'),

    # 3. Auditoría (Solo listado, como indicó el profesor para regiones/países)
    path('grupo_auditoria/listado_auditorias', views.AuditoriaListView.as_view(), name='listado_auditorias'),

    # 4. Ejercicios
    path('grupo_ejercicio/listado_ejercicios', views.EjercicioListView.as_view(), name='listado_ejercicios'),
    path('grupo_ejercicio/crear_ejercicio', views.EjercicioCreateView.as_view(), name='crear_ejercicio'),
    path('grupo_ejercicio/<int:pk>/modificar_ejercicio', views.EjercicioUpdateView.as_view(), name='modificar_ejercicio'),
    path('grupo_ejercicio/<int:pk>/detalle_ejercicio', views.EjercicioDetailView.as_view(), name='detalle_ejercicio'),
    path('grupo_ejercicio/<int:pk>/deshabilitar_ejercicio', views.EjercicioDeshabilitarView.as_view(), name='deshabilitar_ejercicio'),

    # 5. Perfiles
    path('grupo_perfil/listado_perfiles', views.PerfilListView.as_view(), name='listado_perfiles'),
    path('grupo_perfil/crear_perfil', views.PerfilCreateView.as_view(), name='crear_perfil'),
    path('grupo_perfil/<int:pk>/modificar_perfil', views.PerfilUpdateView.as_view(), name='modificar_perfil'),
    path('grupo_perfil/<int:pk>/detalle_perfil', views.PerfilDetailView.as_view(), name='detalle_perfil'),
    path('grupo_perfil/<int:pk>/deshabilitar_perfil', views.PerfilDeshabilitarView.as_view(), name='deshabilitar_perfil'),

    # 6. Planes de Entrenamiento
    path('grupo_plan/listado_planes', views.PlanListView.as_view(), name='listado_planes'),
    path('grupo_plan/crear_plan', views.PlanCreateView.as_view(), name='crear_plan'),
    path('grupo_plan/<int:pk>/modificar_plan', views.PlanUpdateView.as_view(), name='modificar_plan'),
    path('grupo_plan/<int:pk>/detalle_plan', views.PlanDetailView.as_view(), name='detalle_plan'),
    path('grupo_plan/<int:pk>/deshabilitar_plan', views.PlanDeshabilitarView.as_view(), name='deshabilitar_plan'),

    # 7. Progreso Histórico
    path('grupo_progreso/listado_progresos', views.ProgresoListView.as_view(), name='listado_progresos'),
    path('grupo_progreso/crear_progreso', views.ProgresoCreateView.as_view(), name='crear_progreso'),
    path('grupo_progreso/<int:pk>/modificar_progreso', views.ProgresoUpdateView.as_view(), name='modificar_progreso'),
    path('grupo_progreso/<int:pk>/detalle_progreso', views.ProgresoDetailView.as_view(), name='detalle_progreso'),
    path('grupo_progreso/<int:pk>/deshabilitar_progreso', views.ProgresoDeshabilitarView.as_view(), name='deshabilitar_progreso'),

    # 8. Rutinas (Detalle)
    path('grupo_rutina/listado_rutinas', views.RutinaListView.as_view(), name='listado_rutinas'),
    path('grupo_rutina/crear_rutina', views.RutinaCreateView.as_view(), name='crear_rutina'),
    path('grupo_rutina/<int:pk>/modificar_rutina', views.RutinaUpdateView.as_view(), name='modificar_rutina'),
    path('grupo_rutina/<int:pk>/detalle_rutina', views.RutinaDetailView.as_view(), name='detalle_rutina'),
    path('grupo_rutina/<int:pk>/deshabilitar_rutina', views.RutinaDeshabilitarView.as_view(), name='deshabilitar_rutina'),
]