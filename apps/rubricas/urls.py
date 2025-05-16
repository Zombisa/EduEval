from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TblRubricaViewSet, TblCriterioViewSet, TblNivelViewSet, ResultaapRubricaViewSet

router = DefaultRouter()
router.register(r'rubrica', TblRubricaViewSet, basename='rubrica')
router.register(r'criterio', TblCriterioViewSet, basename='criterio')
router.register(r'nivel', TblNivelViewSet, basename='nivel')
router.register(r'resultadorubrica', ResultaapRubricaViewSet, basename='resultadorubrica')

urlpatterns = [
    path('', include(router.urls)),
]
