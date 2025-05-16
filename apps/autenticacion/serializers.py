from rest_framework import serializers
from .models import TblDocente

class TblDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblDocente
        fields = '__all__'
