from rest_framework import serializers
from .models import Rubrica, Criterio, NivelDesempeno


class NivelDesempenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelDesempeno
        fields = ['id', 'nivel', 'descripcion']


class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterio
        fields = ['id', 'rubrica', 'descripcion', 'ponderado', 'nivel']


class RubricaSerializer(serializers.ModelSerializer):
    criterios = CriterioSerializer(many=True, read_only=True)

    class Meta:
        model = Rubrica
        fields = ['id', 'nombre', 'descripcion', 'criterios']
