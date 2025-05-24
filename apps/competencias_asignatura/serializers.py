from rest_framework import serializers
from .models import Asignatura, CompetenciaAsignatura, ResultadoAprendizajeAsignatura, CompetenciaPrograma

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
    competencias_programa = serializers.PrimaryKeyRelatedField(
        queryset=CompetenciaPrograma.objects.all(), many=True, required=False
    )
    class Meta:
        model = CompetenciaAsignatura
        fields = ['id', 'nombre', 'descripcion', 'asignatura', 'competencias_programa']
