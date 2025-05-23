from rest_framework import viewsets
from .models import CompetenciaPrograma, ResultadoAprendizajePrograma
from .serializers import CompetenciaProgramaSerializer, ResultadoAprendizajeProgramaSerializer

class CompetenciaProgramaViewSet(viewsets.ModelViewSet):
    queryset = CompetenciaPrograma.objects.all()
    serializer_class = CompetenciaProgramaSerializer

class ResultadoAprendizajeProgramaViewSet(viewsets.ModelViewSet):
    queryset = ResultadoAprendizajePrograma.objects.all()
    serializer_class = ResultadoAprendizajeProgramaSerializer
