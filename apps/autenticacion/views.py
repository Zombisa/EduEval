from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import TblDocente
from .serializers import TblDocenteSerializer
from rest_framework.response import Response


class TblDocenteViewSet(viewsets.ModelViewSet):
    queryset = TblDocente.objects.all()
    serializer_class = TblDocenteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activo']  # permite usar ?activo=true o ?activo=false

    def destroy(self, request, *args, **kwargs):
        docente = self.get_object()
        docente.activo = False
        docente.save()
        return Response(status=204)
