from django.db import models

class TblDocente(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_tipoidentificacion = models.CharField(max_length=50)
    doc_tipodocente = models.CharField(max_length=50)
    doc_nombres = models.CharField(max_length=100)
    doc_apellidos = models.CharField(max_length=100)
    doc_identificacion = models.CharField(max_length=100)
    doc_titulo = models.CharField(max_length=100)

    class Meta:
        db_table = 'TBL_DOCENTE'
