from django.db import models

class AsigCompDocente(models.Model):
    asig_id = models.IntegerField()
    doc_id = models.IntegerField()
    comp_id = models.IntegerField()
    periodo = models.CharField(max_length=20)

    class Meta:
        db_table = 'ASIG_COMP_DOCENTE'
        unique_together = (('asig_id', 'doc_id', 'comp_id'),)

class TblAsignatura(models.Model):
    asig_id = models.AutoField(primary_key=True)
    asig_nombre = models.CharField(max_length=100)
    asig_creditos = models.IntegerField(null=True, blank=True)
    asig_objetivos = models.CharField(max_length=500, null=True, blank=True)
    asig_semestre = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TBL_ASIGNATURA'
