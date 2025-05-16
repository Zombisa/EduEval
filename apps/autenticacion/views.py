from django.shortcuts import render
from rest_framework import viewsets
from .models import TblDocente
from .serializers import TblDocenteSerializer

class TblDocenteViewSet(viewsets.ModelViewSet):
    queryset = TblDocente.objects.all()
    serializer_class = TblDocenteSerializer

