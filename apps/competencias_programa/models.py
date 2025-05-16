from django.db import models


class TblCompetencia(models.Model):
    comp_id = models.IntegerField(null=False)
    tbl_comp_id = models.IntegerField(null=True)
    comp_descripcion = models.CharField(null=True, max_length=250)
    comp_tipo = models.CharField(null=True, max_length=50)
    comp_nivel = models.CharField(null=True, max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'TBL_COMPETENCIA'
