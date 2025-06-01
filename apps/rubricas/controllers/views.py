from rest_framework.views import APIView
from ..services_facade import fachadas
from ..services_facade.permissions import IsDocente, IsCoordinador

class CrearRubricaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def post(self, request):
        return fachadas.crear_rubrica_con_criterios(request.data)

class ActualizarRubricaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def put(self, request, rubrica_id):
        return fachadas.actualizar_rubrica_y_criterios(rubrica_id, request.data)

class ListarRubricasView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request):
        return fachadas.listar_rubricas()

class ObtenerRubricaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, id):
        return fachadas.obtener_rubrica(id)

class EliminarRubricaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def delete(self, request, id):
        return fachadas.eliminar_rubrica(id)

class ListarNivelesDesempenoView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request):
        return fachadas.listar_niveles_desempeno()
