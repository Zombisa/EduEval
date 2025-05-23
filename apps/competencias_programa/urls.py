from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompetenciaProgramaViewSet, ResultadoAprendizajeProgramaViewSet

router = DefaultRouter()
router.register(r'competencias', CompetenciaProgramaViewSet, basename='competencia-programa')
router.register(r'resultados', ResultadoAprendizajeProgramaViewSet, basename='resultado-programa')

urlpatterns = [
    path('', include(router.urls)),
]
