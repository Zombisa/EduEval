from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluacionViewSet, DetalleEvaluacionViewSet

router = DefaultRouter()
router.register(r'evaluaciones', EvaluacionViewSet, basename='evaluacion')
router.register(r'detalles', DetalleEvaluacionViewSet, basename='detalle-evaluacion')

urlpatterns = [
    path('', include(router.urls)),
]
