from django.urls import path
from .controllers.views import (
    CompetenciaProgramaCreateView,
    CompetenciaProgramaDeleteView,
    CompetenciaProgramaListView,
    ResultadoAprendizajeProgramaCreateView,
    ResultadoAprendizajeProgramaListView,
    ResultadoAprendizajeProgramaDisableView,
    ResultadoAprendizajeProgramaUpdateView,
    ResultadoAprendizajeProgramaDeleteView,
    CopiarResultadoAprendizajeProgramaView,
    CompetenciaProgramaDetailView,
)

urlpatterns = [
    path('crear/', CompetenciaProgramaCreateView.as_view(), name='crear_competencia_programa'),
    path('listar/', CompetenciaProgramaListView.as_view(), name='listar_competencias_programa'),
    path('eliminar/<int:pk>/', CompetenciaProgramaDeleteView.as_view(), name='eliminar_competencia_programa'),
    path('competencias-programa/<int:pk>/', CompetenciaProgramaDetailView.as_view(), name='competencia-programa-detail'),

    path('resultados-aprendizaje/crear/', ResultadoAprendizajeProgramaCreateView.as_view(), name='crear_ra_programa'),
    path('resultados-aprendizaje/listar/', ResultadoAprendizajeProgramaListView.as_view(), name='listar_ra_programa'),
    path('resultados-aprendizaje/desvincular/<int:pk>/', ResultadoAprendizajeProgramaDisableView.as_view(), name='desvincular_ra_programa'),
    path('resultados-aprendizaje/editar/<int:pk>/', ResultadoAprendizajeProgramaUpdateView.as_view(), name='editar_ra_programa'),
    path('resultados-aprendizaje/eliminar/<int:pk>/', ResultadoAprendizajeProgramaDeleteView.as_view(), name='eliminar_ra_programa'),
    path('copiar-ra/<int:resultado_id>/a/<int:competencia_id>/', CopiarResultadoAprendizajeProgramaView.as_view(), name='copiar_ra_programa'),
]
