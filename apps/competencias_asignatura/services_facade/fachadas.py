from ..models.models import CompetenciaAsignatura, ResultadoAprendizajeAsignatura
from ..DTO.serializers import CompetenciaAsignaturaSerializer, ResultadoAprendizajeAsignaturaSerializer
from rest_framework.response import Response
from rest_framework import status

def crear_competencia_asignatura(data):
    resultados_data = data.pop('resultados_aprendizaje', [])
    serializer = CompetenciaAsignaturaSerializer(data=data)
    if serializer.is_valid():
        competencia = serializer.save()
        for resultado in resultados_data:
            ResultadoAprendizajeAsignatura.objects.create(competencia=competencia, **resultado)
        return Response(CompetenciaAsignaturaSerializer(competencia).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def listar_competencias_asignatura(request):
    competencias = CompetenciaAsignatura.objects.all()
    serializer = CompetenciaAsignaturaSerializer(competencias, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def obtener_competencia_asignatura(pk):
    try:
        competencia = CompetenciaAsignatura.objects.get(pk=pk)
        serializer = CompetenciaAsignaturaSerializer(competencia)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CompetenciaAsignatura.DoesNotExist:
        return Response(
            {"detail": "Competencia no encontrada."},
            status=status.HTTP_404_NOT_FOUND
        )

def listar_resultados_aprendizaje_asignatura(request):
    resultados = ResultadoAprendizajeAsignatura.objects.all()
    serializer = ResultadoAprendizajeAsignaturaSerializer(resultados, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def eliminar_competencia_asignatura(pk):
    try:
        competencia = CompetenciaAsignatura.objects.get(pk=pk)
    except CompetenciaAsignatura.DoesNotExist:
        return Response({'error': 'Competencia no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    resultados = ResultadoAprendizajeAsignatura.objects.filter(competencia=competencia)
    for resultado in resultados:
        resultado.competencia = None
        resultado.activo = False
        resultado.save()

    competencia.delete()
    return Response({'mensaje': 'Competencia eliminada y resultados de aprendizaje desactivados'}, status=status.HTTP_200_OK)

    
def crear_resultado_aprendizaje(data):
    serializer = ResultadoAprendizajeAsignaturaSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def listar_resultados_aprendizaje():
    resultados = ResultadoAprendizajeAsignatura.objects.all()
    serializer = ResultadoAprendizajeAsignaturaSerializer(resultados, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def listar_resultados_aprendizaje_activos():
    resultados = ResultadoAprendizajeAsignatura.objects.filter(activo=True)
    serializer = ResultadoAprendizajeAsignaturaSerializer(resultados, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def desvincular_resultado_aprendizaje(pk):
    try:
        resultado = ResultadoAprendizajeAsignatura.objects.get(pk=pk)
        resultado.competencia = None
        resultado.activo = False
        resultado.save()
        return Response({'mensaje': 'Resultado desvinculado correctamente'}, status=status.HTTP_200_OK)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return Response({'error': 'No existe el resultado'}, status=status.HTTP_404_NOT_FOUND)

def eliminar_resultado_aprendizaje(pk):
    try:
        resultado = ResultadoAprendizajeAsignatura.objects.get(pk=pk)
        resultado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return Response({'error': 'No existe el resultado'}, status=status.HTTP_404_NOT_FOUND)
    
def actualizar_resultado_aprendizaje_asignatura(pk, data):
    try:
        resultado = ResultadoAprendizajeAsignatura.objects.get(pk=pk)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return Response({'error': 'Resultado de aprendizaje no encontrado'}, status=404)
    
    serializer = ResultadoAprendizajeAsignaturaSerializer(resultado, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)

def copiar_resultado_aprendizaje_asignatura(resultado_id, competencia_id):
    try:
        resultado = ResultadoAprendizajeAsignatura.objects.get(id=resultado_id)
        competencia = CompetenciaAsignatura.objects.get(id=competencia_id)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return Response({'error': 'Resultado de aprendizaje no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except CompetenciaAsignatura.DoesNotExist:
        return Response({'error': 'Competencia no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    nuevo_resultado = ResultadoAprendizajeAsignatura.objects.create(
        descripcion=resultado.descripcion,
        competencia=competencia,
        activo=True
    )

    serializer = ResultadoAprendizajeAsignaturaSerializer(nuevo_resultado)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


