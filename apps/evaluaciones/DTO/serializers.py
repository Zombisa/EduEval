from rest_framework import serializers
from ..models.models import Evaluacion, ResultadoEvaluacion

class ResultadoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluacion
        fields = ['id', 'criterio', 'nivel_seleccionado', 'nota', 'evaluacion']

class EvaluacionSerializer(serializers.ModelSerializer):
    resultados = ResultadoEvaluacionSerializer(many=True, read_only=True)

    class Meta:
        model = Evaluacion
        fields = ['id', 'rubrica', 'estudiante', 'evaluador', 'fecha', 'retroalimentacion', 'activo', 'resultados']
