from django.shortcuts import render
from rest_framework import viewsets
from .models import TblCompetencia
from .serializers import TblCompetenciaSerializer

class TblCompetenciaViewSet(viewsets.ModelViewSet):
    queryset = TblCompetencia.objects.all()
    serializer_class = TblCompetenciaSerializer
