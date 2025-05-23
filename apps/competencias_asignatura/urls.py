from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet, CompetenciaAsignaturaViewSet, ResultadoAprendizajeAsignaturaViewSet

router = DefaultRouter()
router.register(r'asignaturas', AsignaturaViewSet, basename='asignatura')
router.register(r'competencias', CompetenciaAsignaturaViewSet, basename='competencia-asignatura')
router.register(r'resultados', ResultadoAprendizajeAsignaturaViewSet, basename='resultado-asignatura')

urlpatterns = [
    path('', include(router.urls)),
]
