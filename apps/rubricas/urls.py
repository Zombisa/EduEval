from django.urls import path
from .controllers.views import (
    CrearRubricaView,
    ActualizarRubricaView,
    ListarRubricasView,
    ObtenerRubricaView,
    EliminarRubricaView,
    ListarNivelesDesempenoView,
    RubricasPorRAAsignaturaView,
    ListarCriteriosPorRubricaView,
    AgregarCriterioView,
    VincularRubricaAResultadoView,
    ListarRubricasPorAsignaturaView,
)

urlpatterns = [
    path('crear/', CrearRubricaView.as_view(), name='crear_rubrica'),
    path('actualizar/<int:rubrica_id>/', ActualizarRubricaView.as_view(), name='actualizar_rubrica'),
    path('listar/', ListarRubricasView.as_view(), name='listar_rubricas'),
    path('obtener/<int:id>/', ObtenerRubricaView.as_view(), name='obtener_rubrica'),
    path('eliminar/<int:id>/', EliminarRubricaView.as_view(), name='eliminar_rubrica'),
    path('niveles/', ListarNivelesDesempenoView.as_view(), name='listar_niveles_desempeno'),
    path('por-ra-asignatura/<int:pk>/', RubricasPorRAAsignaturaView.as_view()),
    path("criterios/por-rubrica/<int:rubrica_id>/", ListarCriteriosPorRubricaView.as_view()),
    path("criterios/agregar/", AgregarCriterioView.as_view()),
    path("vincular-a-ra/<int:rubrica_id>/", VincularRubricaAResultadoView.as_view()),
    path("por-asignatura/<int:id_asignatura>/", ListarRubricasPorAsignaturaView.as_view()),
]
