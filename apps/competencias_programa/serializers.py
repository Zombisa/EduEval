from rest_framework import serializers
from .models import CompetenciaPrograma, ResultadoAprendizajePrograma

class ResultadoAprendizajeProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizajePrograma
        fields = '__all__'

class CompetenciaProgramaSerializer(serializers.ModelSerializer):
    resultado_aprendizaje = ResultadoAprendizajeProgramaSerializer(read_only=True)

    class Meta:
        model = CompetenciaPrograma
        fields = '__all__'

    def create(self, validated_data):
        # Crear la competencia primero
        competencia = CompetenciaPrograma.objects.create(**validated_data)

        # Crear automáticamente el resultado de aprendizaje relacionado
        ResultadoAprendizajePrograma.objects.create(
            competencia=competencia,
            descripcion=f"Resultado de aprendizaje para: {competencia.nombre}"
        )
        return competencia
