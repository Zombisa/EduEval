# Generated by Django 5.2.1 on 2025-05-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAsignatura',
            fields=[
                ('asig_id', models.AutoField(primary_key=True, serialize=False)),
                ('asig_nombre', models.CharField(max_length=100)),
                ('asig_creditos', models.IntegerField(blank=True, null=True)),
                ('asig_objetivos', models.CharField(blank=True, max_length=500, null=True)),
                ('asig_semestre', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TBL_ASIGNATURA',
            },
        ),
        migrations.CreateModel(
            name='AsigCompDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asig_id', models.IntegerField()),
                ('doc_id', models.IntegerField()),
                ('comp_id', models.IntegerField()),
                ('periodo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'ASIG_COMP_DOCENTE',
                'unique_together': {('asig_id', 'doc_id', 'comp_id')},
            },
        ),
    ]
