from django.shortcuts import render
from rest_framework import viewsets
from .models import TblCompetencia
from .serializers import TblCompetenciaSerializer
from rest_framework.response import Response

class TblCompetenciaViewSet(viewsets.ModelViewSet):
    queryset = TblCompetencia.objects.filter(activo=True)
    serializer_class = TblCompetenciaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)
