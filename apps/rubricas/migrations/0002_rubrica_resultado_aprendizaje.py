# Generated by Django 5.2.1 on 2025-06-05 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competencias_asignatura', '0002_competenciaasignatura_programa'),
        ('rubricas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubrica',
            name='resultado_aprendizaje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rubricas', to='competencias_asignatura.resultadoaprendizajeasignatura'),
        ),
    ]
