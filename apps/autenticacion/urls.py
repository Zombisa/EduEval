from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .controllers.views import vista_evaluador, vista_profesor, vista_general

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('protegido/evaluador/', vista_evaluador),
    path('protegido/profesor/', vista_profesor),
    path('protegido/general/', vista_general),
]
