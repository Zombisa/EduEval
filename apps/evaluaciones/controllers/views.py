from rest_framework.views import APIView
from ..services_facade import fachadas
from ..services_facade.permissions import IsCoordinador, IsEvaluadorExterno, IsDocente

class EvaluacionCreateView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def post(self, request):
        return fachadas.crear_evaluacion(request.data)

class EvaluacionListView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def get(self, request):
        return fachadas.listar_evaluaciones()

class EvaluacionRetrieveView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def get(self, request, pk):
        return fachadas.obtener_evaluacion(pk)

class EvaluacionUpdateView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def put(self, request, pk):
        return fachadas.actualizar_evaluacion(pk, request.data)

class EvaluacionDeleteView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def delete(self, request, pk):
        return fachadas.eliminar_evaluacion(pk)

class EvaluacionListAllView(APIView):  # Lista incluso las desactivadas
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def get(self, request):
        return fachadas.listar_todas_las_evaluaciones()

class NivelDesempenoListView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def get(self, request):
        return fachadas.listar_niveles_desempeno()

class EvaluacionRetrieveView(APIView):
    permission_classes = [IsCoordinador | IsDocente | IsEvaluadorExterno]
    def get(self, request, pk):
        return fachadas.obtener_evaluacion(pk)
