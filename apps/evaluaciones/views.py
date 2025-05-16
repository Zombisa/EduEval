from django.shortcuts import render
from rest_framework import viewsets
from .models import EvaluacionPlaceholder
from .serializers import EvaluacionPlaceholderSerializer

class EvaluacionPlaceholderViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionPlaceholder.objects.all()
    serializer_class = EvaluacionPlaceholderSerializer
