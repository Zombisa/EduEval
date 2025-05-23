# Generated by Django 5.2.1 on 2025-05-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCriterio',
            fields=[
                ('idcriterio', models.AutoField(primary_key=True, serialize=False)),
                ('idrubrica', models.CharField(max_length=10)),
                ('cri_descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TBL_CRITERIO',
            },
        ),
        migrations.CreateModel(
            name='TblNivel',
            fields=[
                ('idnivel', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TBL_NIVEL',
            },
        ),
        migrations.CreateModel(
            name='TblRubrica',
            fields=[
                ('idrubrica', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('rub_descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'TBL_RUBRICA',
            },
        ),
        migrations.CreateModel(
            name='ResultaapRubrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rap_id', models.IntegerField()),
                ('idrubrica', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'RESULTAAP_RUBRICA',
                'unique_together': {('rap_id', 'idrubrica')},
            },
        ),
    ]
