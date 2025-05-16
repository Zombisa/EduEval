from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluacionPlaceholderViewSet

router = DefaultRouter()
router.register(r'evaluacionevaluacion', EvaluacionPlaceholderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
