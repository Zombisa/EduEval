from rest_framework import viewsets
from .models import Rubrica, Criterio, Nivel
from .serializers import RubricaSerializer, CriterioSerializer, NivelSerializer

class RubricaViewSet(viewsets.ModelViewSet):
    queryset = Rubrica.objects.all()
    serializer_class = RubricaSerializer

class CriterioViewSet(viewsets.ModelViewSet):
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
