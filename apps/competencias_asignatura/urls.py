from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsigCompDocenteViewSet, TblAsignaturaViewSet

router = DefaultRouter()
router.register(r'asignaciondocente', AsigCompDocenteViewSet, basename='asignaciondocente')
router.register(r'asignatura', TblAsignaturaViewSet, basename='asignatura')  

urlpatterns = [
    path('', include(router.urls)),
]