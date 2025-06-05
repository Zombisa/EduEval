from rest_framework import serializers
from ..models.models import CompetenciaPrograma, ResultadoAprendizajePrograma

class ResultadoAprendizajeProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizajePrograma
        fields = ['id', 'descripcion', 'activo', 'fecha_creacion', 'competencia']
        read_only_fields = ['id', 'fecha_creacion']

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción del resultado de aprendizaje no puede estar vacía.")
        return value

class CompetenciaProgramaSerializer(serializers.ModelSerializer):
    resultados_aprendizaje = ResultadoAprendizajeProgramaSerializer(many=True, read_only=True)

    class Meta:
        model = CompetenciaPrograma
        fields = ['id', 'descripcion', 'id_programa', 'nivel', 'resultados_aprendizaje']
        read_only_fields = ['id']

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción no puede estar vacía.")
        return value

    def validate_id_programa(self, value):
        if value <= 0:
            raise serializers.ValidationError("El ID del programa debe ser un número positivo.")
        return value
