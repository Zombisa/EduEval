from rest_framework import serializers
from ..models.models import Rubrica, Criterio, NivelDesempeno


class NivelDesempenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelDesempeno
        fields = ['id', 'nivel', 'descripcion']


class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterio
        fields = '__all__'


class RubricaSerializer(serializers.ModelSerializer):
    criterios = CriterioSerializer(many=True, read_only=True)

    class Meta:
        model = Rubrica
        fields = ['id', 'nombre', 'descripcion', 'criterios']

class RubricaVincularRASerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubrica
        fields = ['resultado_aprendizaje']

