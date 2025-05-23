from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Asignatura, CompetenciaAsignatura, ResultadoAprendizajeAsignatura
from .serializers import AsignaturaSerializer, CompetenciaAsignaturaSerializer, ResultadoAprendizajeAsignaturaSerializer

class CompetenciaAsignaturaViewSet(viewsets.ModelViewSet):
    queryset = CompetenciaAsignatura.objects.all()
    serializer_class = CompetenciaAsignaturaSerializer

class ResultadoAprendizajeAsignaturaViewSet(viewsets.ModelViewSet):
    queryset = ResultadoAprendizajeAsignatura.objects.all()
    serializer_class = ResultadoAprendizajeAsignaturaSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['semestre']

