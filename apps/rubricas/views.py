from django.shortcuts import render
from rest_framework import viewsets
from .models import TblRubrica, TblCriterio, TblNivel, ResultaapRubrica
from .serializers import TblRubricaSerializer, TblCriterioSerializer, TblNivelSerializer, ResultaapRubricaSerializer

class TblRubricaViewSet(viewsets.ModelViewSet):
    queryset = TblRubrica.objects.all()
    serializer_class = TblRubricaSerializer

class TblCriterioViewSet(viewsets.ModelViewSet):
    queryset = TblCriterio.objects.all()
    serializer_class = TblCriterioSerializer

class TblNivelViewSet(viewsets.ModelViewSet):
    queryset = TblNivel.objects.all()
    serializer_class = TblNivelSerializer

class ResultaapRubricaViewSet(viewsets.ModelViewSet):
    queryset = ResultaapRubrica.objects.all()
    serializer_class = ResultaapRubricaSerializer
