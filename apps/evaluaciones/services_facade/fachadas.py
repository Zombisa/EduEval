from rest_framework.response import Response
from rest_framework import status
from ..models.models import Evaluacion, ResultadoEvaluacion
from ..DTO.serializers import EvaluacionSerializer, ResultadoEvaluacionSerializer
from apps.rubricas.models.models import Criterio, NivelDesempeno
from apps.rubricas.DTO.serializers import NivelDesempenoSerializer

def crear_evaluacion(data):
    resultados_data = data.pop('resultados', [])
    serializer = EvaluacionSerializer(data=data)

    if serializer.is_valid():
        evaluacion = serializer.save()

        for resultado in resultados_data:
            resultado_obj = ResultadoEvaluacion(
                evaluacion=evaluacion,
                criterio_id=resultado['criterio'],
                nivel_seleccionado_id=resultado['nivel_seleccionado'],
                nota=resultado['nota']
            )
            resultado_obj.save()
        return Response(EvaluacionSerializer(evaluacion).data, status=status.HTTP_201_CREATED)

    return Response({
        'error': 'Evaluación inválida',
        'detalle': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


def listar_evaluaciones():
    evaluaciones = Evaluacion.objects.filter(activo=True)
    serializer = EvaluacionSerializer(evaluaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def obtener_evaluacion(pk):
    try:
        evaluacion = Evaluacion.objects.get(pk=pk)
        serializer = EvaluacionSerializer(evaluacion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Evaluacion.DoesNotExist:
        return Response({'error': 'Evaluación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

def actualizar_evaluacion(pk, data):
    try:
        evaluacion = Evaluacion.objects.get(pk=pk)
    except Evaluacion.DoesNotExist:
        return Response({'error': 'Evaluación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    resultados_data = data.pop('resultados', [])
    serializer = EvaluacionSerializer(evaluacion, data=data, partial=True)

    if serializer.is_valid():
        evaluacion = serializer.save()

        # Eliminar resultados anteriores
        ResultadoEvaluacion.objects.filter(evaluacion=evaluacion).delete()

        for resultado in resultados_data:
            resultado['evaluacion'] = evaluacion.id  # <- clave para evitar el error
            resultado_serializer = ResultadoEvaluacionSerializer(data=resultado)
            if resultado_serializer.is_valid():
                resultado_serializer.save()
            else:
                return Response({
                    'error': 'Resultado inválido',
                    'detalle': resultado_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response(EvaluacionSerializer(evaluacion).data, status=status.HTTP_200_OK)

    return Response({
        'error': 'Evaluación inválida',
        'detalle': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)



def eliminar_evaluacion(pk):
    try:
        evaluacion = Evaluacion.objects.get(pk=pk)
        evaluacion.activo = False
        evaluacion.save()
        return Response({'mensaje': 'Evaluación desactivada'}, status=status.HTTP_200_OK)
    except Evaluacion.DoesNotExist:
        return Response({'error': 'Evaluación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

def listar_todas_las_evaluaciones():  # incluye inactivas
    evaluaciones = Evaluacion.objects.all()
    serializer = EvaluacionSerializer(evaluaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def listar_niveles_desempeno():
    niveles = NivelDesempeno.objects.all()
    serializer = NivelDesempenoSerializer(niveles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def obtener_evaluacion(pk):
    try:
        evaluacion = Evaluacion.objects.get(pk=pk)
        serializer = EvaluacionSerializer(evaluacion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Evaluacion.DoesNotExist:
        return Response({'error': 'Evaluación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

