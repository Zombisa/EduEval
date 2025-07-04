"""
Controladores para la gestión de rúbricas, criterios y niveles de desempeño.
Estas vistas exponen endpoints REST que delegan la lógica a la capa de fachada.
"""
from rest_framework import generics
from rest_framework.views import APIView
from ..services_facade import fachadas
from ..services_facade.permissions import IsDocente, IsCoordinador
from rest_framework.response import Response

class CrearRubricaView(APIView):
    """
    POST api/rubricas/crear/
    Crea una nueva rúbrica junto con sus criterios.
    """
    permission_classes = [IsCoordinador | IsDocente]
    def post(self, request):
        return fachadas.crear_rubrica_con_criterios(request.data)

class ActualizarRubricaView(APIView):
    """
    PUT api/rubricas/actualizar/<int:rubrica_id>/
    Actualiza una rúbrica y reemplaza sus criterios.
    """
    permission_classes = [IsCoordinador | IsDocente]
    def put(self, request, rubrica_id):
        return fachadas.actualizar_rubrica_y_criterios(rubrica_id, request.data)

class ListarRubricasView(APIView):
    """
    GET api/rubricas/listar/
    Lista todas las rúbricas registradas.
    """
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request):
        return fachadas.listar_rubricas()

class ObtenerRubricaView(APIView):
    """
    GET api/rubricas/obtener/<int:id>/
    Retorna una rúbrica específica por su ID.
    """
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, id):
        return fachadas.obtener_rubrica(id)

class EliminarRubricaView(APIView):
    """
    DELETE api/rubricas/eliminar/<int:id>/
    Elimina una rúbrica por su ID.
    """
    permission_classes = [IsCoordinador | IsDocente]
    def delete(self, request, id):
        return fachadas.eliminar_rubrica(id)

class ListarNivelesDesempenoView(APIView):
    """
    GET api/rubricas/niveles/
    Lista los niveles de desempeño disponibles.
    """
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request):
        return fachadas.listar_niveles_desempeno()

class RubricasPorRAAsignaturaView(APIView):
    """
    GET api/rubricas/por-ra-asignatura/<int:pk>/
    Lista todas las rúbricas asociadas a un resultado de aprendizaje de asignatura.
    """
    def get(self, request, pk):
        return fachadas.listar_rubricas_por_ra(pk)
    
class ListarCriteriosPorRubricaView(APIView):
    """
    GET api/rubricas/criterios/por-rubrica/<int:rubrica_id>/
    Lista los criterios asociados a una rúbrica.
    """
    permission_classes = [IsDocente | IsCoordinador]
    def get(self, request, rubrica_id):
        return fachadas.listar_criterios_por_rubrica(rubrica_id)

class AgregarCriterioView(APIView):
    """
    POST api/rubricas/criterios/agregar/
    Agrega un nuevo criterio a una rúbrica existente.
    """
    permission_classes = [IsDocente | IsCoordinador]
    def post(self, request):
        return fachadas.agregar_criterio_a_rubrica(request.data)
    
class VincularRubricaARaView(APIView):
    permission_classes = [IsDocente | IsCoordinador]
    def patch(self, request, ra_id):
        rubrica_id = request.data.get("rubrica")
        if not rubrica_id:
            return Response({"error": "ID de rúbrica no proporcionado"}, status=400)
        return fachadas.vincular_rubrica_a_ra(ra_id, rubrica_id)

class ListarRubricasPorAsignaturaView(APIView):
    permission_classes = [IsDocente | IsCoordinador]
    """
    GET /api/rubricas/por-asignatura/<int:id_asignatura>/
    Lista todas las rúbricas asociadas a los resultados de aprendizaje 
    de la asignatura con ese ID.
    """
    def get(self, request, id_asignatura):
        return fachadas.listar_rubricas_por_asignatura(id_asignatura)

class RubricaPorRAView(APIView):
    permission_classes = [IsDocente | IsCoordinador]

    def get(self, request, ra_id):
        return fachadas.obtener_rubrica_por_ra(ra_id)
    

class CriterioCreateView(APIView):
    permission_classes = [IsCoordinador | IsDocente]

    def post(self, request):
        return fachadas.crear_criterio_para_rubrica(request.data)