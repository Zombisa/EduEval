from rest_framework import status
from .models import CompetenciaPrograma, ResultadoAprendizajePrograma
from .serializers import (
    CompetenciaProgramaSerializer,
    ResultadoAprendizajeProgramaSerializer
)
from django.utils import timezone


def crear_competencia_programa(data):
    try:
        serializer = CompetenciaProgramaSerializer(data=data)
        if serializer.is_valid():
            competencia = serializer.save()
            ResultadoAprendizajePrograma.objects.create(
                competencia_programa=competencia,
                descripcion="",
                activo=True
            )
            return {"data": serializer.data, "status": status.HTTP_201_CREATED}
        return {"data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        return {"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST}


def listar_competencias_programa():
    competencias = CompetenciaPrograma.objects.all()
    return CompetenciaProgramaSerializer(competencias, many=True).data


def eliminar_competencia_programa(pk):
    try:
        competencia = CompetenciaPrograma.objects.get(pk=pk)
        competencia.resultados_aprendizaje.update(competencia_programa=None)
        competencia.delete()
        return {"data": {"mensaje": "Competencia eliminada."}, "status": status.HTTP_200_OK}
    except CompetenciaPrograma.DoesNotExist:
        return {"data": {"error": "Competencia no encontrada."}, "status": status.HTTP_404_NOT_FOUND}
    except Exception as e:
        return {"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST}


def crear_resultado_aprendizaje_programa(data):
    try:
        serializer = ResultadoAprendizajeProgramaSerializer(data=data)
        if serializer.is_valid():
            serializer.save(fecha_creacion=timezone.now(), activo=True)
            return {"data": serializer.data, "status": status.HTTP_201_CREATED}
        return {"data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}
    except Exception as e:
        return {"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST}


def listar_resultados_aprendizaje_programa(mostrar_todos=False):
    if mostrar_todos:
        resultados = ResultadoAprendizajePrograma.objects.all()
    else:
        resultados = ResultadoAprendizajePrograma.objects.filter(activo=True)
    return ResultadoAprendizajeProgramaSerializer(resultados, many=True).data


def desvincular_resultado_aprendizaje_programa(pk):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
        resultado.competencia_programa = None
        resultado.activo = False
        resultado.save()
        return {"data": {"mensaje": "Resultado de aprendizaje desvinculado."}, "status": status.HTTP_200_OK}
    except ResultadoAprendizajePrograma.DoesNotExist:
        return {"data": {"error": "Resultado de aprendizaje no encontrado."}, "status": status.HTTP_404_NOT_FOUND}
    except Exception as e:
        return {"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST}


def eliminar_resultado_aprendizaje_programa(pk):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
        resultado.delete()
        return {"data": {"mensaje": "Resultado de aprendizaje eliminado."}, "status": status.HTTP_200_OK}
    except ResultadoAprendizajePrograma.DoesNotExist:
        return {"data": {"error": "Resultado de aprendizaje no encontrado."}, "status": status.HTTP_404_NOT_FOUND}
    except Exception as e:
        return {"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST}

def actualizar_resultado_aprendizaje_programa(pk, data):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
    except ResultadoAprendizajePrograma.DoesNotExist:
        return {'error': 'Resultado no encontrado'}, 404

    serializer = ResultadoAprendizajeProgramaSerializer(resultado, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, 200
    return serializer.errors, 400

def copiar_resultado_aprendizaje_programa(resultado_id, nueva_competencia_id):
    try:
        resultado_original = ResultadoAprendizajePrograma.objects.get(pk=resultado_id)
        competencia_destino = CompetenciaPrograma.objects.get(pk=nueva_competencia_id)
    except ResultadoAprendizajePrograma.DoesNotExist:
        return {'error': 'Resultado original no encontrado'}, 404
    except CompetenciaPrograma.DoesNotExist:
        return {'error': 'Competencia destino no encontrada'}, 404

    resultado_copiado = ResultadoAprendizajePrograma.objects.create(
        competencia=competencia_destino,
        descripcion=resultado_original.descripcion,
        activo=True
    )
    serializer = ResultadoAprendizajeProgramaSerializer(resultado_copiado)
    return serializer.data, 201
