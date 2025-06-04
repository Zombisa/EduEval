from rest_framework.views import APIView
from ..services_facade import fachadas
from ..services_facade.permissions import IsCoordinador

class CompetenciaProgramaCreateView(APIView):
    permission_classes = [IsCoordinador]
    def post(self, request):
        return fachadas.crear_competencia_programa(request.data)

class CompetenciaProgramaDeleteView(APIView):
    permission_classes = [IsCoordinador]
    def delete(self, request, pk):
        return fachadas.eliminar_competencia_programa(pk)

class CompetenciaProgramaListView(APIView):    
    permission_classes = [IsCoordinador]
    def get(self, request):
        return fachadas.listar_competencias_programa()
    
class CompetenciaProgramaDetailView(APIView):
    permission_classes = [IsCoordinador]
    def get(self, request, pk):
        return fachadas.obtener_competencia_programa(pk)

class ResultadoAprendizajeProgramaCreateView(APIView):
    permission_classes = [IsCoordinador]
    def post(self, request):
        return fachadas.crear_resultado_aprendizaje_programa(request.data)

class ResultadoAprendizajeProgramaListView(APIView):
    permission_classes = [IsCoordinador]
    def get(self, request):
        incluir_inactivos = request.query_params.get('incluir_inactivos') == 'true'
        return fachadas.listar_resultados_aprendizaje_programa(incluir_inactivos)

class ResultadoAprendizajeProgramaDisableView(APIView):
    permission_classes = [IsCoordinador]
    def patch(self, request, pk):
        return fachadas.desvincular_resultado_aprendizaje_programa(pk)

class ResultadoAprendizajeProgramaDeleteView(APIView):
    permission_classes = [IsCoordinador]
    def delete(self, request, pk):
        return fachadas.eliminar_resultado_aprendizaje_programa(pk)

class ResultadoAprendizajeProgramaUpdateView(APIView):
    permission_classes = [IsCoordinador]
    def put(self, request, pk):
        return fachadas.editar_resultado_aprendizaje_programa(pk, request.data)

class CopiarResultadoAprendizajeProgramaView(APIView):
    permission_classes = [IsCoordinador]
    def post(self, request, resultado_id, competencia_id):
        return fachadas.copiar_resultado_aprendizaje_programa(resultado_id, competencia_id)
