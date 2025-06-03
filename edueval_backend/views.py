from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import logout
from django.shortcuts import redirect

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    return Response({'message': f'🎉 ¡Hola {request.user.username}! Estás autenticado con JWT.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': f'Hola {request.user.username}, estás autenticado con JWT.'})

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return redirect('/')
