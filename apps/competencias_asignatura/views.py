from django.shortcuts import render
from rest_framework import viewsets
from .models import AsigCompDocente, TblAsignatura
from .serializers import AsigCompDocenteSerializer, TblAsignaturaSerializer
from rest_framework.response import Response

class AsigCompDocenteViewSet(viewsets.ModelViewSet):
    queryset = AsigCompDocente.objects.filter(activo=True)
    serializer_class = AsigCompDocenteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)

class TblAsignaturaViewSet(viewsets.ModelViewSet):
    queryset = TblAsignatura.objects.filter(activo=True)
    serializer_class = TblAsignaturaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)
