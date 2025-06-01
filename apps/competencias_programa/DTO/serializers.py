from rest_framework import serializers
from ..models.models import CompetenciaPrograma, ResultadoAprendizajePrograma


class ResultadoAprendizajeProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizajePrograma
        fields = ['id', 'descripcion', 'activo', 'fecha_creacion', 'competencia']


class CompetenciaProgramaSerializer(serializers.ModelSerializer):
    resultados_aprendizaje = ResultadoAprendizajeProgramaSerializer(many=True, read_only=True)

    class Meta:
        model = CompetenciaPrograma
        fields = ['id', 'descripcion', 'id_programa', 'nivel', 'resultados_aprendizaje']
