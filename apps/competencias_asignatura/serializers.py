from rest_framework import serializers
from .models import AsigCompDocente, TblAsignatura

class AsigCompDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsigCompDocente
        fields = '__all__'

class TblAsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAsignatura
        fields = '__all__'
