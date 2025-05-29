from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import TblDocente
from .serializers import TblDocenteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def prueba_callback(request):
    return JsonResponse({"status": "Django sí responde a /oidc/callback/"})


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
    

#Solo para evaluadores
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@user_passes_test(lambda u: u.groups.filter(name='evaluador').exists())
def vista_evaluador(request):
    return JsonResponse({'mensaje': f'Hola evaluador {request.user.username}, puedes acceder a evaluaciones.'})

#Solo para profesores o coordinadores
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@user_passes_test(lambda u: u.groups.filter(name='profesor').exists())
def vista_profesor(request):
    return JsonResponse({'mensaje': f'Hola profesor/coordinador {request.user.username}, puedes administrar el sistema.'})

#Para cualquier usuario autenticado (login exitoso, sin validar grupo)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vista_general(request):
    return JsonResponse({'mensaje': f'Hola {request.user.username}, sesión iniciada correctamente.'})

