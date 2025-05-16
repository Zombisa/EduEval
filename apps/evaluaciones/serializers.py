from rest_framework import serializers
from .models import EvaluacionPlaceholder

class EvaluacionPlaceholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluacionPlaceholder
        fields = '__all__'
