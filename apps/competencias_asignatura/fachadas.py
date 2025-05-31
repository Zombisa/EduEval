from .models import CompetenciaAsignatura, ResultadoAprendizajeAsignatura
from .serializers import CompetenciaAsignaturaSerializer, ResultadoAprendizajeAsignaturaSerializer
from rest_framework.response import Response
from rest_framework import status

def crear_competencia_asignatura(data):
    serializer = CompetenciaAsignaturaSerializer(data=data)
    if serializer.is_valid():
        competencia = serializer.save()
        ResultadoAprendizajeAsignatura.objects.create(
            competencia=competencia,
            descripcion="",
            nivel=1,
            activo=True
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def listar_competencias_asignatura():
    competencias = CompetenciaAsignatura.objects.all()
    serializer = CompetenciaAsignaturaSerializer(competencias, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def eliminar_competencia_asignatura(pk):
    try:
        competencia = CompetenciaAsignatura.objects.get(pk=pk)
        competencia.resultados_aprendizaje.update(competencia=None)  # desvincula
        competencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except CompetenciaAsignatura.DoesNotExist:
        return Response({'error': 'No existe la competencia'}, status=status.HTTP_404_NOT_FOUND)
    
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
        return {'error': 'Resultado no encontrado'}, 404

    serializer = ResultadoAprendizajeAsignaturaSerializer(resultado, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, 200
    return serializer.errors, 400

def copiar_resultado_aprendizaje_asignatura(resultado_id, nueva_competencia_id):
    try:
        resultado_original = ResultadoAprendizajeAsignatura.objects.get(pk=resultado_id)
        competencia_destino = CompetenciaAsignatura.objects.get(pk=nueva_competencia_id)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return {'error': 'Resultado original no encontrado'}, 404
    except CompetenciaAsignatura.DoesNotExist:
        return {'error': 'Competencia destino no encontrada'}, 404

    resultado_copiado = ResultadoAprendizajeAsignatura.objects.create(
        competencia=competencia_destino,
        descripcion=resultado_original.descripcion,
        activo=True
    )
    serializer = ResultadoAprendizajeAsignaturaSerializer(resultado_copiado)
    return serializer.data, 201

