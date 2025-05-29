from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TblDocenteViewSet
from .views import vista_evaluador, vista_profesor, vista_general

router = DefaultRouter()
router.register(r'docente', TblDocenteViewSet, basename='docente')

urlpatterns = [
    path('', include(router.urls)),
    path('protegido/evaluador/', vista_evaluador),
    path('protegido/profesor/', vista_profesor),
    path('protegido/general/', vista_general),
]
