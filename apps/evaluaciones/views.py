from django.shortcuts import render
from rest_framework import viewsets
from .models import EvaluacionPlaceholder
from .serializers import EvaluacionPlaceholderSerializer
from rest_framework.response import Response

class EvaluacionPlaceholderViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionPlaceholder.objects.filter(activo=True)
    serializer_class = EvaluacionPlaceholderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return Response(status=204)
