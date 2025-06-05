from rest_framework.views import APIView
from ..services_facade import fachadas
from ..services_facade.permissions import IsCoordinador, IsDocente
from ..models.models import ResultadoAprendizajeAsignatura

class CompetenciaAsignaturaCreateView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def post(self, request):
        return fachadas.crear_competencia_asignatura(request.data)
    
class CompetenciaAsignaturaListView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request):
        return fachadas.listar_competencias_asignatura(request)

class CompetenciaAsignaturaDetailView(APIView):
    permission_classes = [IsCoordinador]
    def get(self, request, pk):
        return fachadas.obtener_competencia_asignatura(pk)

class CompetenciaAsignaturaDeleteView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def delete(self, request, pk):
        return fachadas.eliminar_competencia_asignatura(pk)

class ResultadoAprendizajeAsignaturaCreateView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def post(self, request):
        return fachadas.crear_resultado_aprendizaje(request.data)

class ResultadoAprendizajeAsignaturaListView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request):
        incluir_inactivos = request.query_params.get('incluir_inactivos') == 'true'
        return fachadas.listar_resultados_aprendizaje_asignatura(incluir_inactivos)

class ResultadoAprendizajeAsignaturaDisableView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def patch(self, request, pk):
        return fachadas.desvincular_resultado_aprendizaje(pk)

class ResultadoAprendizajeAsignaturaDeleteView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def delete(self, request, pk):
        return fachadas.eliminar_resultado_aprendizaje(pk)

class ResultadoAprendizajeAsignaturaUpdateView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def put(self, request, pk):
        return fachadas.actualizar_resultado_aprendizaje_asignatura(pk, request.data)

class CopiarResultadoAprendizajeAsignaturaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def post(self, request, resultado_id, competencia_id):
        return fachadas.copiar_resultado_aprendizaje_asignatura(resultado_id, competencia_id)
    
class ResultadoAprendizajePorCompetenciaAsignaturaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, pk):
        return fachadas.listar_ra_por_competencia_asignatura(pk)
    
class CompetenciaAsignaturaDesdeRAView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, pk):
        return fachadas.obtener_competencia_asignatura_desde_ra(pk)
    
class AsociarProgramaACompetenciaAsignaturaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def patch(self, request, pk):
        return fachadas.asociar_programa_a_competencia_asignatura(pk, request.data)
    
class CompetenciasPorAsignaturaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, id_asignatura):
        return fachadas.listar_competencias_por_asignatura(id_asignatura)

class RAporAsignaturaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, id_asignatura):
        return fachadas.listar_ra_por_asignatura(id_asignatura)

class CompetenciasYRAAsignaturaView(APIView):
    permission_classes = [IsCoordinador | IsDocente]
    def get(self, request, id_asignatura):
        return fachadas.listar_competencias_y_ra_por_asignatura(id_asignatura)

    