"""
Módulo de fachada para la gestión de rúbricas y criterios en el sistema EduEval.
Incluye funciones para crear, actualizar, listar, eliminar y vincular rúbricas
con resultados de aprendizaje, así como manejar criterios y niveles de desempeño.
"""
from rest_framework.response import Response
from rest_framework import status
from ..models.models import Rubrica, Criterio, NivelDesempeno
from ..DTO.serializers import RubricaSerializer, CriterioSerializer, NivelDesempenoSerializer
from apps.competencias_asignatura.models.models import ResultadoAprendizajeAsignatura

def crear_rubrica_con_criterios(data):
    """
    Crea una rúbrica con sus criterios asociados.
    
    Args:
        data (dict): Diccionario que incluye los campos de la rúbrica y una lista de criterios.
    
    Returns:
        Response: Objeto JSON con la rúbrica creada o errores de validación.
    """
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
    """
    Actualiza una rúbrica existente junto con sus criterios.
    
    Args:
        rubrica_id (int): ID de la rúbrica a actualizar.
        data (dict): Datos nuevos de la rúbrica y lista de criterios.
    
    Returns:
        Response: Rúbrica actualizada o errores.
    """
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
    """
    Lista todas las rúbricas del sistema.

    Returns:
        Response: Lista serializada de rúbricas.
    """
    rubricas = Rubrica.objects.all()
    serializer = RubricaSerializer(rubricas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def obtener_rubrica(id):
    """
    Obtiene una rúbrica por su ID.

    Args:
        id (int): ID de la rúbrica.

    Returns:
        Response: Datos de la rúbrica o error.
    """
    try:
        rubrica = Rubrica.objects.get(id=id)
        serializer = RubricaSerializer(rubrica)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Rubrica.DoesNotExist:
        return Response({'error': 'Rúbrica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

def eliminar_rubrica(id):
    """
    Elimina una rúbrica por su ID.

    Args:
        id (int): ID de la rúbrica.

    Returns:
        Response: Mensaje de confirmación o error.
    """
    try:
        rubrica = Rubrica.objects.get(id=id)
        rubrica.delete()
        return Response({'mensaje': 'Rúbrica eliminada'}, status=status.HTTP_200_OK)
    except Rubrica.DoesNotExist:
        return Response({'error': 'Rúbrica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

def listar_niveles_desempeno():
    """
    Lista todos los niveles de desempeño disponibles.

    Returns:
        Response: Lista de niveles.
    """
    niveles = NivelDesempeno.objects.all()
    serializer = NivelDesempenoSerializer(niveles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def listar_rubricas_por_ra(pk):
    """
    Lista todas las rúbricas asociadas a un Resultado de Aprendizaje.

    Args:
        pk (int): ID del RA.

    Returns:
        Response: Lista de rúbricas.
    """
    rubricas = Rubrica.objects.filter(resultado_aprendizaje_id=pk)
    serializer = RubricaSerializer(rubricas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def listar_criterios_por_rubrica(rubrica_id):
    """
    Lista todos los criterios de una rúbrica específica.

    Args:
        rubrica_id (int): ID de la rúbrica.

    Returns:
        Response: Lista de criterios.
    """
    criterios = Criterio.objects.filter(rubrica_id=rubrica_id)
    serializer = CriterioSerializer(criterios, many=True)
    return Response(serializer.data)

def agregar_criterio_a_rubrica(data):
    """
    Agrega un nuevo criterio a una rúbrica existente.

    Args:
        data (dict): Datos del criterio.

    Returns:
        Response: Criterio creado o errores.
    """
    serializer = CriterioSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def vincular_rubrica_a_ra(ra_id, rubrica_id):
    try:
        ra = ResultadoAprendizajeAsignatura.objects.get(pk=ra_id)
        rubrica = Rubrica.objects.get(pk=rubrica_id)
        ra.rubrica = rubrica
        ra.save()
        return Response({"message": "Rúbrica vinculada correctamente al resultado de aprendizaje."}, status=200)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return Response({"error": "Resultado de aprendizaje no encontrado"}, status=404)
    except Rubrica.DoesNotExist:
        return Response({"error": "Rúbrica no encontrada"}, status=404)

def obtener_rubrica_por_ra(ra_id):
    try:
        ra = ResultadoAprendizajeAsignatura.objects.get(pk=ra_id)
        if ra.rubrica:
            serializer = RubricaSerializer(ra.rubrica)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Este RA no tiene rúbrica asignada."}, status=status.HTTP_204_NO_CONTENT)
    except ResultadoAprendizajeAsignatura.DoesNotExist:
        return Response({"error": "Resultado de aprendizaje no encontrado."}, status=status.HTTP_404_NOT_FOUND)