from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RubricaViewSet, CriterioViewSet, NivelViewSet

router = DefaultRouter()
router.register(r'rubricas', RubricaViewSet, basename='rubrica')
router.register(r'criterios', CriterioViewSet, basename='criterio')
router.register(r'niveles', NivelViewSet, basename='nivel')

urlpatterns = [
    path('', include(router.urls)),
]
