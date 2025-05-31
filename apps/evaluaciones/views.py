from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import fachadas

class EvaluacionCreateView(APIView):
    def post(self, request):
        return fachadas.crear_evaluacion(request.data)

class EvaluacionListView(APIView):
    def get(self, request):
        return fachadas.listar_evaluaciones()

class EvaluacionRetrieveView(APIView):
    def get(self, request, pk):
        return fachadas.obtener_evaluacion(pk)

class EvaluacionUpdateView(APIView):
    def put(self, request, pk):
        return fachadas.actualizar_evaluacion(pk, request.data)

class EvaluacionDeleteView(APIView):
    def delete(self, request, pk):
        return fachadas.eliminar_evaluacion(pk)

class EvaluacionListAllView(APIView):  # Lista incluso las desactivadas
    def get(self, request):
        return fachadas.listar_todas_las_evaluaciones()

class NivelDesempenoListView(APIView):
    def get(self, request):
        return fachadas.listar_niveles_desempeno()
