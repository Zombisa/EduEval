from rest_framework import serializers
from ..models.models import CompetenciaAsignatura, ResultadoAprendizajeAsignatura
from apps.rubricas.models.models import Rubrica
from apps.rubricas.DTO.serializers import RubricaSerializer

class ResultadoAprendizajeAsignaturaSerializer(serializers.ModelSerializer):
    # Mostrar la rúbrica completa al hacer GET
    rubrica = RubricaSerializer(read_only=True)

    # Permitir enviar solo el ID de la rúbrica al hacer POST o PUT
    rubrica_id = serializers.PrimaryKeyRelatedField(
        source='rubrica',
        queryset=Rubrica.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = ResultadoAprendizajeAsignatura
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion']

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción del resultado de aprendizaje no puede estar vacía.")
        return value

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

    def validate_id_asignatura(self, value):
        if value <= 0:
            raise serializers.ValidationError("El ID de asignatura debe ser un número positivo.")
        return value

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción no puede estar vacía.")
        return value
