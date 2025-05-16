from rest_framework import serializers
from .models import TblRubrica, TblCriterio, TblNivel, ResultaapRubrica

class TblRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblRubrica
        fields = '__all__'

class TblCriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCriterio
        fields = '__all__'

class TblNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblNivel
        fields = '__all__'

class ResultaapRubricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultaapRubrica
        fields = '__all__'
