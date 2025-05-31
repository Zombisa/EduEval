from rest_framework import serializers
from .models import Evaluacion, ResultadoEvaluacion

class ResultadoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluacion
        fields = ['id', 'criterio', 'nivel_seleccionado', 'nota']

class EvaluacionSerializer(serializers.ModelSerializer):
    resultados = ResultadoEvaluacionSerializer(many=True)

    class Meta:
        model = Evaluacion
        fields = ['id', 'rubrica', 'estudiante', 'evaluador_id', 'fecha', 'retroalimentacion', 'activo', 'resultados']
