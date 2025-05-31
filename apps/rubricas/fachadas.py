from rest_framework.response import Response
from rest_framework import status
from .models import Rubrica, Criterio, NivelDesempeno
from .serializers import RubricaSerializer, CriterioSerializer, NivelDesempenoSerializer

def crear_rubrica_con_criterios(data):
    criterios_data = data.pop('criterios', [])
    rubrica_serializer = RubricaSerializer(data=data)
    
    if not rubrica_serializer.is_valid():
        return Response({'error': 'Rúbrica inválida', 'detalle': rubrica_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    rubrica = rubrica_serializer.save()
    
    for criterio_data in criterios_data:
        criterio_data['rubrica'] = rubrica.id
        serializer_criterio = CriterioSerializer(data=criterio_data)
        if serializer_criterio.is_valid():
            serializer_criterio.save()
        else:
            return Response({'error': 'Criterio inválido', 'detalle': serializer_criterio.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(RubricaSerializer(rubrica).data, status=status.HTTP_201_CREATED)

def actualizar_rubrica_y_criterios(rubrica_id, data):
    try:
        rubrica = Rubrica.objects.get(id=rubrica_id)
    except Rubrica.DoesNotExist:
        return Response({'error': 'Rúbrica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    criterios_data = data.pop('criterios', [])

    rubrica_serializer = RubricaSerializer(rubrica, data=data, partial=True)
    if not rubrica_serializer.is_valid():
        return Response({'error': 'Rúbrica inválida', 'detalle': rubrica_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    rubrica = rubrica_serializer.save()

    # Eliminar criterios existentes para actualizar con los nuevos
    Criterio.objects.filter(rubrica=rubrica).delete()

    for criterio_data in criterios_data:
        criterio_data['rubrica'] = rubrica.id
        serializer_criterio = CriterioSerializer(data=criterio_data)
        if serializer_criterio.is_valid():
            serializer_criterio.save()
        else:
            return Response({'error': 'Criterio inválido', 'detalle': serializer_criterio.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(RubricaSerializer(rubrica).data, status=status.HTTP_200_OK)

def listar_rubricas():
    rubricas = Rubrica.objects.all()
    serializer = RubricaSerializer(rubricas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def obtener_rubrica(id):
    try:
        rubrica = Rubrica.objects.get(id=id)
        serializer = RubricaSerializer(rubrica)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Rubrica.DoesNotExist:
        return Response({'error': 'Rúbrica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

def eliminar_rubrica(id):
    try:
        rubrica = Rubrica.objects.get(id=id)
        rubrica.delete()
        return Response({'mensaje': 'Rúbrica eliminada'}, status=status.HTTP_200_OK)
    except Rubrica.DoesNotExist:
        return Response({'error': 'Rúbrica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

def listar_niveles_desempeno():
    niveles = NivelDesempeno.objects.all()
    serializer = NivelDesempenoSerializer(niveles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
