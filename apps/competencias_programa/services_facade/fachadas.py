from rest_framework.response import Response
from rest_framework import status
from ..models.models import CompetenciaPrograma, ResultadoAprendizajePrograma
from ..DTO.serializers import (
    CompetenciaProgramaSerializer,
    ResultadoAprendizajeProgramaSerializer
)
from django.utils import timezone


def crear_competencia_programa(data):
    try:
        resultados_data = data.pop('resultados_aprendizaje', [])

        serializer = CompetenciaProgramaSerializer(data=data)
        if serializer.is_valid():
            competencia = serializer.save()

            for resultado in resultados_data:
                resultado['competencia'] = competencia.id
                resultado_serializer = ResultadoAprendizajeProgramaSerializer(data=resultado)
                if resultado_serializer.is_valid():
                    resultado_serializer.save()
                else:
                    return Response({
                        'error': 'Resultado de aprendizaje inválido',
                        'detalle': resultado_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response(CompetenciaProgramaSerializer(competencia).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def listar_competencias_programa():
    competencias = CompetenciaPrograma.objects.all()
    return Response(CompetenciaProgramaSerializer(competencias, many=True).data)

def obtener_competencia_programa_desde_ra(pk):
    try:
        ra = ResultadoAprendizajePrograma.objects.get(pk=pk)
        competencia = ra.competencia
        if competencia is None:
            return Response({"detail": "Este RA no está asociado a ninguna competencia."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompetenciaProgramaSerializer(competencia)
        return Response(serializer.data)
    except ResultadoAprendizajePrograma.DoesNotExist:
        return Response({"detail": "Resultado de aprendizaje no encontrado."}, status=status.HTTP_404_NOT_FOUND)

def listar_ra_por_competencia_programa(pk):
    ra = ResultadoAprendizajePrograma.objects.filter(competencia_id=pk)
    serializer = ResultadoAprendizajeProgramaSerializer(ra, many=True)
    return Response(serializer.data)


def obtener_competencia_programa(pk):
    try:
        competencia = CompetenciaPrograma.objects.get(pk=pk)
        serializer = CompetenciaProgramaSerializer(competencia)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CompetenciaPrograma.DoesNotExist:
        return Response(
            {"detail": "Competencia no encontrada."},
            status=status.HTTP_404_NOT_FOUND
        )


def eliminar_competencia_programa(pk):
    try:
        competencia = CompetenciaPrograma.objects.get(pk=pk)
        competencia.resultados_aprendizaje.update(competencia=None)
        competencia.delete()
        return Response({"data": {"mensaje": "Competencia eliminada."}, "status": status.HTTP_200_OK})
    except CompetenciaPrograma.DoesNotExist:
        return Response({"data": {"error": "Competencia no encontrada."}, "status": status.HTTP_404_NOT_FOUND})
    except Exception as e:
        return Response({"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST})


def crear_resultado_aprendizaje_programa(data):
    try:
        serializer = ResultadoAprendizajeProgramaSerializer(data=data)
        if serializer.is_valid():
            serializer.save(fecha_creacion=timezone.now(), activo=True)
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})
        return Response({"data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
    except Exception as e:
        return Response({"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST})


def listar_resultados_aprendizaje_programa(incluir_inactivos=False):
    if incluir_inactivos:
        resultados = ResultadoAprendizajePrograma.objects.all()
    else:
        resultados = ResultadoAprendizajePrograma.objects.filter(activo=True)

    serializer = ResultadoAprendizajeProgramaSerializer(resultados, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



def desvincular_resultado_aprendizaje_programa(pk):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
        resultado.competencia = None
        resultado.activo = False
        resultado.save()
        return Response({"data": {"mensaje": "Resultado de aprendizaje desvinculado."}, "status": status.HTTP_200_OK})
    except ResultadoAprendizajePrograma.DoesNotExist:
        return Response({"data": {"error": "Resultado de aprendizaje no encontrado."}, "status": status.HTTP_404_NOT_FOUND})
    except Exception as e:
        return Response({"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST})


def eliminar_resultado_aprendizaje_programa(pk):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
        resultado.delete()
        return Response({"data": {"mensaje": "Resultado de aprendizaje eliminado."}, "status": status.HTTP_200_OK})
    except ResultadoAprendizajePrograma.DoesNotExist:
        return Response({"data": {"error": "Resultado de aprendizaje no encontrado."}, "status": status.HTTP_404_NOT_FOUND})
    except Exception as e:
        return Response({"data": {"error": str(e)}, "status": status.HTTP_400_BAD_REQUEST})

def actualizar_resultado_aprendizaje_programa(pk, data):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
    except ResultadoAprendizajePrograma.DoesNotExist:
        return Response({'error': 'Resultado no encontrado'}, 404)

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
        return Response({'error': 'Resultado original no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except CompetenciaPrograma.DoesNotExist:
        return Response({'error': 'Competencia destino no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    nuevo_data = {
        'descripcion': resultado_original.descripcion,
        'competencia': competencia_destino.id,
        'activo': True
    }

    serializer = ResultadoAprendizajeProgramaSerializer(data=nuevo_data)
    if serializer.is_valid():
        resultado_copiado = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def editar_resultado_aprendizaje_programa(pk, data):
    try:
        resultado = ResultadoAprendizajePrograma.objects.get(pk=pk)
    except ResultadoAprendizajePrograma.DoesNotExist:
        return Response(
            {"data": {"error": "Resultado de aprendizaje no encontrado."}},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = ResultadoAprendizajeProgramaSerializer(resultado, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"data": {"error": serializer.errors}},
            status=status.HTTP_400_BAD_REQUEST
        )
    
def listar_competencias_programa_por_programa(id_programa):
    competencias = CompetenciaPrograma.objects.filter(id_programa=id_programa)
    serializer = CompetenciaProgramaSerializer(competencias, many=True)
    return Response(serializer.data)

def listar_ra_programa_por_programa(id_programa):
    ra = ResultadoAprendizajePrograma.objects.filter(competencia__id_programa=id_programa)
    serializer = ResultadoAprendizajeProgramaSerializer(ra, many=True)
    return Response(serializer.data)

def listar_competencias_y_ra_programa_por_programa(id_programa):
    competencias = CompetenciaPrograma.objects.filter(id_programa=id_programa)
    serializer = CompetenciaProgramaSerializer(competencias, many=True)
    return Response(serializer.data)