from django.urls import path
from .controllers.views import (
    CompetenciaAsignaturaCreateView,
    CompetenciaAsignaturaDeleteView,
    CompetenciaAsignaturaListView,
    CompetenciaAsignaturaDetailView,
    ResultadoAprendizajeAsignaturaCreateView,
    ResultadoAprendizajeAsignaturaListView,
    ResultadoAprendizajeAsignaturaDisableView,
    ResultadoAprendizajeAsignaturaDeleteView,
    ResultadoAprendizajeAsignaturaUpdateView,
    CopiarResultadoAprendizajeAsignaturaView,
)

urlpatterns = [
    path('crear/', CompetenciaAsignaturaCreateView.as_view(), name='crear_competencia_asignatura'),
    path('listar/', CompetenciaAsignaturaListView.as_view(), name='listar_competencias_asignatura'),
    path('competencias-asignatura/<int:pk>/', CompetenciaAsignaturaDetailView.as_view(), name='competencia-asignatura-detail'),
    path('eliminar/<int:pk>/', CompetenciaAsignaturaDeleteView.as_view(), name='eliminar_competencia_asignatura'),
    
    path('resultados-aprendizaje/crear/', ResultadoAprendizajeAsignaturaCreateView.as_view(), name='crear_ra_asignatura'),
    path('resultados-aprendizaje/listar/', ResultadoAprendizajeAsignaturaListView.as_view(), name='listar_ra_asignatura'),
    path('resultados-aprendizaje/desvincular/<int:pk>/', ResultadoAprendizajeAsignaturaDisableView.as_view(), name='desvincular_ra_asignatura'),
    path('resultados-aprendizaje/eliminar/<int:pk>/', ResultadoAprendizajeAsignaturaDeleteView.as_view(), name='eliminar_ra_asignatura'),
    path('resultados-aprendizaje/editar/<int:pk>/', ResultadoAprendizajeAsignaturaUpdateView.as_view(), name='editar_ra_asignatura'),
    path('copiar-ra/<int:resultado_id>/a/<int:competencia_id>/', CopiarResultadoAprendizajeAsignaturaView.as_view(), name='copiar_ra_asignatura'),
]
