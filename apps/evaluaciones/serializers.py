from rest_framework import serializers
from .models import Evaluacion, DetalleEvaluacion
from apps.rubricas.models import Rubrica
from apps.rubricas.serializers import RubricaSerializer
from apps.competencias_programa.models import ResultadoAprendizajePrograma
from apps.competencias_asignatura.models import ResultadoAprendizajeAsignatura

class EvaluacionSerializer(serializers.ModelSerializer):
    rubrica = RubricaSerializer(read_only=True)
    rubrica_id = serializers.PrimaryKeyRelatedField(
        queryset=Rubrica.objects.all(), source='rubrica', write_only=True
    )

    resultado_aprendizaje_programa_id = serializers.PrimaryKeyRelatedField(
        queryset=ResultadoAprendizajePrograma.objects.all(),
        source='resultado_aprendizaje_programa',
        write_only=True,
        required=False,
        allow_null=True
    )

    resultado_aprendizaje_asignatura_id = serializers.PrimaryKeyRelatedField(
        queryset=ResultadoAprendizajeAsignatura.objects.all(),
        source='resultado_aprendizaje_asignatura',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Evaluacion
        fields = [
            'id',
            'fecha',
            'rubrica', 'rubrica_id',
            'resultado_aprendizaje_programa_id',
            'resultado_aprendizaje_asignatura_id'
        ]

class DetalleEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleEvaluacion
        fields = '__all__'
