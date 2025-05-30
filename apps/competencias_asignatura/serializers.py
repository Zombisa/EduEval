from rest_framework import serializers
from .models import CompetenciaAsignatura, ResultadoAprendizajeAsignatura


class ResultadoAprendizajeAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizajeAsignatura
        fields = [
            'id',
            'descripcion',
            'activo',
            'fecha_creacion',
            'competencia'
        ]
        read_only_fields = ['id', 'fecha_creacion']


class CompetenciaAsignaturaSerializer(serializers.ModelSerializer):
    resultados_aprendizaje = ResultadoAprendizajeAsignaturaSerializer(many=True, read_only=True)

    class Meta:
        model = CompetenciaAsignatura
        fields = [
            'id',
            'id_asignatura',
            'descripcion',
            'nivel',
            'resultados_aprendizaje'
        ]
        read_only_fields = ['id']
