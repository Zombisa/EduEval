from rest_framework import serializers
from ..models.models import CompetenciaAsignatura, ResultadoAprendizajeAsignatura

class ResultadoAprendizajeAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizajeAsignatura
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion']


class CompetenciaAsignaturaSerializer(serializers.ModelSerializer):
    resultados_aprendizaje = ResultadoAprendizajeAsignaturaSerializer(many=True, required=False)

    class Meta:
        model = CompetenciaAsignatura
        fields = [
            'id',
            'id_asignatura',
            'descripcion',
            'nivel',
            'programa',
            'resultados_aprendizaje'
        ]
        read_only_fields = ['id']

