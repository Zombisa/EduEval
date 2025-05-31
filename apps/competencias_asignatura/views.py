from rest_framework.views import APIView
from . import fachadas

class CompetenciaAsignaturaCreateView(APIView):
    def post(self, request):
        return fachadas.crear_competencia_asignatura(request.data)

class CompetenciaAsignaturaDeleteView(APIView):
    def delete(self, request, pk):
        return fachadas.eliminar_competencia_asignatura(pk)

class ResultadoAprendizajeAsignaturaCreateView(APIView):
    def post(self, request):
        return fachadas.crear_resultado_aprendizaje_asignatura(request.data)

class ResultadoAprendizajeAsignaturaListView(APIView):
    def get(self, request):
        incluir_inactivos = request.query_params.get('incluir_inactivos') == 'true'
        return fachadas.listar_resultados_aprendizaje_asignatura(incluir_inactivos)

class ResultadoAprendizajeAsignaturaDisableView(APIView):
    def post(self, request, pk):
        return fachadas.desvincular_resultado_aprendizaje_asignatura(pk)

class ResultadoAprendizajeAsignaturaDeleteView(APIView):
    def delete(self, request, pk):
        return fachadas.eliminar_resultado_aprendizaje_asignatura(pk)

class ResultadoAprendizajeAsignaturaUpdateView(APIView):
    def put(self, request, pk):
        return fachadas.editar_resultado_aprendizaje_asignatura(pk, request.data)

class CopiarResultadoAprendizajeAsignaturaView(APIView):
    def post(self, request, resultado_id, competencia_id):
        return fachadas.copiar_resultado_aprendizaje_asignatura(resultado_id, competencia_id)
