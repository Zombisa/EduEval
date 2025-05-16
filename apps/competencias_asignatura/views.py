from django.shortcuts import render
from rest_framework import viewsets
from .models import AsigCompDocente, TblAsignatura
from .serializers import AsigCompDocenteSerializer, TblAsignaturaSerializer

class AsigCompDocenteViewSet(viewsets.ModelViewSet):
    queryset = AsigCompDocente.objects.all()
    serializer_class = AsigCompDocenteSerializer

class TblAsignaturaViewSet(viewsets.ModelViewSet):
    queryset = TblAsignatura.objects.all()
    serializer_class = TblAsignaturaSerializer
