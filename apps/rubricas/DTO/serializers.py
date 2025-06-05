from rest_framework import serializers
from ..models.models import Rubrica, Criterio, NivelDesempeno

class NivelDesempenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelDesempeno
        fields = ['id', 'nivel', 'descripcion']

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción no puede estar vacía.")
        return value

class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterio
        fields = '__all__'

    def validate_descripcion(self, value):
        if not value.strip():
            raise serializers.ValidationError("La descripción del criterio no puede estar vacía.")
        return value

    def validate_ponderado(self, value):
        if not (0.0 <= value <= 1.0):
            raise serializers.ValidationError("El valor ponderado debe estar entre 0.0 y 1.0.")
        return value

class RubricaSerializer(serializers.ModelSerializer):
    criterios = CriterioSerializer(many=True, read_only=True)

    class Meta:
        model = Rubrica
        fields = ['id', 'nombre', 'descripcion', 'criterios']

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre de la rúbrica no puede estar vacío.")
        return value

class RubricaVincularRASerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubrica
        fields = ['resultado_aprendizaje']
