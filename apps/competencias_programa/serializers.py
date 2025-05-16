from rest_framework import serializers
from .models import TblCompetencia

class TblCompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCompetencia
        fields = '__all__'
