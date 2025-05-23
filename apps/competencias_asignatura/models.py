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
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='competencias')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class ResultadoAprendizajeAsignatura(models.Model):
    competencia = models.OneToOneField(CompetenciaAsignatura, on_delete=models.CASCADE, related_name='resultado_aprendizaje')
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    relacionados_programa = models.ManyToManyField(ResultadoAprendizajePrograma, blank=True)

    def __str__(self):
        return f"RA de {self.competencia.nombre}"