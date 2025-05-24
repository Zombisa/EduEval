from django.db import models
from apps.competencias_programa.models import CompetenciaPrograma, ResultadoAprendizajePrograma

class Asignatura(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    creditos = models.PositiveIntegerField()
    semestre = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

class CompetenciaAsignatura(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    asignatura = models.ForeignKey("Asignatura", on_delete=models.CASCADE, related_name="competencias")
    
    # NUEVO: relación con competencias del programa
    competencias_programa = models.ManyToManyField(CompetenciaPrograma, related_name="competencias_asignatura")

    def __str__(self):
        return self.nombre


class ResultadoAprendizajeAsignatura(models.Model):
    nombre = models.CharField(max_length=255, default="Nombre temporal")
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    competencia = models.OneToOneField(CompetenciaAsignatura, on_delete=models.CASCADE, related_name='resultado_aprendizaje')
    relacionados_programa = models.ManyToManyField('competencias_programa.ResultadoAprendizajePrograma', blank=True)

    def __str__(self):
        return f"RA de {self.competencia.nombre}"