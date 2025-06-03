from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse

from apps.autenticacion.DTO.serializers import CustomTokenObtainPairSerializer

from ..permissions import IsDocente, IsCoordinador, IsEvaluadorExterno


#  JWT con roles
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


#  Endpoints protegidos por roles
@api_view(['GET'])
@permission_classes([IsEvaluadorExterno])
def vista_evaluador(request):
    return JsonResponse({'mensaje': f'Hola evaluador externo {request.user.username}'})


@api_view(['GET'])
@permission_classes([IsDocente | IsCoordinador])
def vista_profesor(request):
    return JsonResponse({'mensaje': f'Hola docente o coordinador {request.user.username}'})


@api_view(['GET'])
@permission_classes([IsCoordinador | IsDocente | IsEvaluadorExterno])
def vista_general(request):
    return JsonResponse({'mensaje': f'Hola {request.user.username}, sesión iniciada correctamente.'})
