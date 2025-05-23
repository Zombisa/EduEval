from rest_framework import viewsets
from .models import Evaluacion, DetalleEvaluacion
from .serializers import EvaluacionSerializer, DetalleEvaluacionSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class DetalleEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = DetalleEvaluacion.objects.all()
    serializer_class = DetalleEvaluacionSerializer
