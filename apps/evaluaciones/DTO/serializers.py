from rest_framework import serializers
from apps.evaluaciones.models.models import Evaluacion, ResultadoEvaluacion

class ResultadoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluacion
        fields = ['id', 'criterio', 'nivel_seleccionado', 'nota', 'evaluacion']

    def validate_nota(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("La nota debe estar entre 0 y 5.")
        return value

    def validate(self, data):
        if not data.get('criterio'):
            raise serializers.ValidationError({"criterio": "Este campo es obligatorio."})
        if not data.get('evaluacion'):
            raise serializers.ValidationError({"evaluacion": "Este campo es obligatorio."})
        return data

class EvaluacionSerializer(serializers.ModelSerializer):
    resultados = ResultadoEvaluacionSerializer(many=True, read_only=True)

    class Meta:
        model = Evaluacion
        fields = ['id', 'rubrica', 'estudiante', 'evaluador', 'fecha', 'retroalimentacion', 'activo', 'resultados']

    def validate_estudiante(self, value):
        if not value.strip():
            raise serializers.ValidationError("El campo 'estudiante' no puede estar vacío.")
        return value

    def validate_evaluador(self, value):
        if not value.strip():
            raise serializers.ValidationError("El campo 'evaluador' no puede estar vacío.")
        return value

    def validate(self, data):
        if not data.get('rubrica'):
            raise serializers.ValidationError({"rubrica": "La rúbrica es obligatoria."})
        return data
