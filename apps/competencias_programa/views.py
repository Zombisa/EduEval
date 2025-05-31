from rest_framework.views import APIView
from . import fachadas

class CompetenciaProgramaCreateView(APIView):
    def post(self, request):
        return fachadas.crear_competencia_programa(request.data)

class CompetenciaProgramaDeleteView(APIView):
    def delete(self, request, pk):
        return fachadas.eliminar_competencia_programa(pk)

class ResultadoAprendizajeProgramaCreateView(APIView):
    def post(self, request):
        return fachadas.crear_resultado_aprendizaje_programa(request.data)

class ResultadoAprendizajeProgramaListView(APIView):
    def get(self, request):
        incluir_inactivos = request.query_params.get('incluir_inactivos') == 'true'
        return fachadas.listar_resultados_aprendizaje_programa(incluir_inactivos)

class ResultadoAprendizajeProgramaDisableView(APIView):
    def post(self, request, pk):
        return fachadas.desvincular_resultado_aprendizaje_programa(pk)

class ResultadoAprendizajeProgramaDeleteView(APIView):
    def delete(self, request, pk):
        return fachadas.eliminar_resultado_aprendizaje_programa(pk)

class ResultadoAprendizajeProgramaUpdateView(APIView):
    def put(self, request, pk):
        return fachadas.editar_resultado_aprendizaje_programa(pk, request.data)

class CopiarResultadoAprendizajeProgramaView(APIView):
    def post(self, request, resultado_id, competencia_id):
        return fachadas.copiar_resultado_aprendizaje_programa(resultado_id, competencia_id)
