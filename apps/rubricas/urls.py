from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TblRubricaViewSet, TblCriterioViewSet, TblNivelViewSet, ResultaapRubricaViewSet

router = DefaultRouter()
router.register(r'rubrica', TblRubricaViewSet)
router.register(r'criterio', TblCriterioViewSet)
router.register(r'nivel', TblNivelViewSet)
router.register(r'resultadorubrica', ResultaapRubricaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
