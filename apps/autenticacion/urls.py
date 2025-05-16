from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TblDocenteViewSet

router = DefaultRouter()
router.register(r'', TblDocenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
