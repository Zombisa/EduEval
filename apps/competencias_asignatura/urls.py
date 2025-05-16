from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsigCompDocenteViewSet, TblAsignaturaViewSet

router = DefaultRouter()
router.register(r'asignacioncompdocente', AsigCompDocenteViewSet)
router.register(r'asignacionnatura', TblAsignaturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
