from rest_framework import serializers
from .models import Asignatura, CompetenciaAsignatura, ResultadoAprendizajeAsignatura

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class ResultadoAprendizajeAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizajeAsignatura
        fields = '__all__'

class CompetenciaAsignaturaSerializer(serializers.ModelSerializer):
    resultado_aprendizaje = ResultadoAprendizajeAsignaturaSerializer(read_only=True)

    class Meta:
        model = CompetenciaAsignatura
        fields = '__all__'

    def create(self, validated_data):
        competencia = CompetenciaAsignatura.objects.create(**validated_data)
        ResultadoAprendizajeAsignatura.objects.create(
            competencia=competencia,
            descripcion=f"Resultado de aprendizaje para: {competencia.nombre}"
        )
        return competencia
