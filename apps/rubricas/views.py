from django.shortcuts import render
from rest_framework import viewsets
from .models import TblRubrica, TblCriterio, TblNivel, ResultaapRubrica
from .serializers import TblRubricaSerializer, TblCriterioSerializer, TblNivelSerializer, ResultaapRubricaSerializer
from rest_framework.response import Response

class TblRubricaViewSet(viewsets.ModelViewSet):
    queryset = TblRubrica.objects.filter(activo=True)
    serializer_class = TblRubricaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)

class TblCriterioViewSet(viewsets.ModelViewSet):
    queryset = TblCriterio.objects.filter(activo=True)
    serializer_class = TblCriterioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)

class TblNivelViewSet(viewsets.ModelViewSet):
    queryset = TblNivel.objects.filter(activo=True)
    serializer_class = TblNivelSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)

class ResultaapRubricaViewSet(viewsets.ModelViewSet):
    queryset = ResultaapRubrica.objects.filter(activo=True)
    serializer_class = ResultaapRubricaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)
