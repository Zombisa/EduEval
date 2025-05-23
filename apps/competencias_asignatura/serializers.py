from rest_framework import serializers
from .models import Asignatura, CompetenciaAsignatura, ResultadoAprendizajeAsignatura

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class ResultadoAprendizajeAsignaturaSerializer(serializers.ModelSerializer):
    competencia = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ResultadoAprendizajeAsignatura
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'competencia', 'relacionados_programa']

class CompetenciaAsignaturaSerializer(serializers.ModelSerializer):
    resultado_aprendizaje = ResultadoAprendizajeAsignaturaSerializer(write_only=True)

    class Meta:
        model = CompetenciaAsignatura
        fields = ['id', 'nombre', 'descripcion', 'asignatura', 'resultado_aprendizaje']

    def create(self, validated_data):
        resultado_data = validated_data.pop('resultado_aprendizaje')
        competencia = CompetenciaAsignatura.objects.create(**validated_data)
        ResultadoAprendizajeAsignatura.objects.create(competencia=competencia, **resultado_data)
        return competencia
