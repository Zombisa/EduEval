from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TblCompetenciaViewSet

router = DefaultRouter()
router.register(r'competencia', TblCompetenciaViewSet)

router = DefaultRouter()
router.register(r'', TblCompetenciaViewSet, basename='competencia')

urlpatterns = [
    path('', include(router.urls)),
]