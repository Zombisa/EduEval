from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TblCompetenciaViewSet

router = DefaultRouter()
router.register(r'competencia', TblCompetenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
