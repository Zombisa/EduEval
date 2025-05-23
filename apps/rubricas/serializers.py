from rest_framework import serializers
from .models import Rubrica, Criterio, Nivel

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = ['id', 'descripcion', 'puntaje']

class CriterioSerializer(serializers.ModelSerializer):
    niveles = NivelSerializer(many=True)
    
    class Meta:
        model = Criterio
        fields = ['id', 'descripcion', 'rubrica', 'niveles']
        extra_kwargs = {
            'rubrica': {'read_only': True}
        }

    def create(self, validated_data):
        niveles_data = validated_data.pop('niveles')
        criterio = Criterio.objects.create(**validated_data)
        for nivel_data in niveles_data:
            Nivel.objects.create(criterio=criterio, **nivel_data)
        return criterio

    def update(self, instance, validated_data):
        niveles_data = validated_data.pop('niveles', [])
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.save()

        if niveles_data:
            instance.niveles.all().delete()
            for nivel_data in niveles_data:
                Nivel.objects.create(criterio=instance, **nivel_data)

        return instance

class RubricaSerializer(serializers.ModelSerializer):
    criterios = CriterioSerializer(many=True)

    class Meta:
        model = Rubrica
        fields = ['id', 'nombre', 'descripcion', 'criterios']

    def create(self, validated_data):
        criterios_data = validated_data.pop('criterios')
        rubrica = Rubrica.objects.create(**validated_data)
        for criterio_data in criterios_data:
            niveles_data = criterio_data.pop('niveles')
            criterio = Criterio.objects.create(rubrica=rubrica, **criterio_data)
            for nivel_data in niveles_data:
                Nivel.objects.create(criterio=criterio, **nivel_data)
        return rubrica

    def update(self, instance, validated_data):
        criterios_data = validated_data.pop('criterios', [])
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.save()

        if criterios_data:
            instance.criterios.all().delete()
            for criterio_data in criterios_data:
                niveles_data = criterio_data.pop('niveles')
                criterio = Criterio.objects.create(rubrica=instance, **criterio_data)
                for nivel_data in niveles_data:
                    Nivel.objects.create(criterio=criterio, **nivel_data)

        return instance
