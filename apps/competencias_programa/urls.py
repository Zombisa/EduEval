from django.urls import path
from .views import (
    CompetenciaProgramaCreateView,
    CompetenciaProgramaDeleteView,
    ResultadoAprendizajeProgramaCreateView,
    ResultadoAprendizajeProgramaListView,
    ResultadoAprendizajeProgramaDisableView,
    ResultadoAprendizajeProgramaUpdateView,
    ResultadoAprendizajeProgramaDeleteView,
    CopiarResultadoAprendizajeProgramaView,
)

urlpatterns = [
    path('crear/', CompetenciaProgramaCreateView.as_view(), name='crear_competencia_programa'),
    path('eliminar/<int:pk>/', CompetenciaProgramaDeleteView.as_view(), name='eliminar_competencia_programa'),

    path('resultados-aprendizaje/crear/', ResultadoAprendizajeProgramaCreateView.as_view(), name='crear_ra_programa'),
    path('resultados-aprendizaje/listar/', ResultadoAprendizajeProgramaListView.as_view(), name='listar_ra_programa'),
    path('resultados-aprendizaje/desvincular/<int:pk>/', ResultadoAprendizajeProgramaDisableView.as_view(), name='desvincular_ra_programa'),
    path('resultados-aprendizaje/editar/<int:pk>/', ResultadoAprendizajeProgramaUpdateView.as_view(), name='editar_ra_programa'),
    path('resultados-aprendizaje/eliminar/<int:pk>/', ResultadoAprendizajeProgramaDeleteView.as_view(), name='eliminar_ra_programa'),
    path('copiar-ra/<int:resultado_id>/a/<int:competencia_id>/', CopiarResultadoAprendizajeProgramaView.as_view(), name='copiar_ra_programa'),
]
