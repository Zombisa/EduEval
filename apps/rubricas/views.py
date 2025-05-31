from rest_framework.views import APIView
from . import fachadas

class CrearRubricaView(APIView):
    def post(self, request):
        return fachadas.crear_rubrica_con_criterios(request.data)

class ActualizarRubricaView(APIView):
    def put(self, request, rubrica_id):
        return fachadas.actualizar_rubrica_y_criterios(rubrica_id, request.data)

class ListarRubricasView(APIView):
    def get(self, request):
        return fachadas.listar_rubricas()

class ObtenerRubricaView(APIView):
    def get(self, request, id):
        return fachadas.obtener_rubrica(id)

class EliminarRubricaView(APIView):
    def delete(self, request, id):
        return fachadas.eliminar_rubrica(id)

class ListarNivelesDesempenoView(APIView):
    def get(self, request):
        return fachadas.listar_niveles_desempeno()
