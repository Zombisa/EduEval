from django.db import models

class TblRubrica(models.Model):
    idrubrica = models.CharField(max_length=10, primary_key=True)
    rub_descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'TBL_RUBRICA'

class TblCriterio(models.Model):
    idcriterio = models.AutoField(primary_key=True)
    idrubrica = models.CharField(max_length=10)
    cri_descripcion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'TBL_CRITERIO'

class TblNivel(models.Model):
    idnivel = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'TBL_NIVEL'

class ResultaapRubrica(models.Model):
    rap_id = models.IntegerField()
    idrubrica = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'RESULTAAP_RUBRICA'
        unique_together = (('rap_id', 'idrubrica'),)
