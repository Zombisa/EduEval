from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..permissions import IsDocente, IsCoordinador, IsEvaluadorExterno
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def prueba_callback(request):
    return JsonResponse({"status": "Django sí responde a /oidc/callback/"})

@api_view(['GET'])
@permission_classes([IsEvaluadorExterno])
def vista_evaluador(request):
    return JsonResponse({'mensaje': f'Hola evaluador externo {getattr(request, "keycloak_username", request.user.username)}'})

@api_view(['GET'])
@permission_classes([IsDocente | IsCoordinador])
def vista_profesor(request):
    return JsonResponse({'mensaje': f'Hola docente o coordinador {getattr(request, "keycloak_username", request.user.username)}'})

@api_view(['GET'])
@permission_classes([IsCoordinador | IsDocente | IsEvaluadorExterno])
def vista_general(request):
    return JsonResponse({'mensaje': f'Hola {getattr(request, "keycloak_username", request.user.username)}, sesión iniciada correctamente.'})
