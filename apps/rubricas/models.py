from django.db import models
from apps.competencias_asignatura.models import ResultadoAprendizajeAsignatura

class Rubrica(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResultadoAprendizajeAsignatura, on_delete=models.CASCADE, related_name='rubricas')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, related_name='criterios')
    descripcion = models.TextField()

    def __str__(self):
        return f"Criterio de {self.rubrica.nombre}"

class Nivel(models.Model):
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE, related_name='niveles')
    descripcion = models.TextField()
    valor = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Nivel {self.valor} - {self.criterio.rubrica.nombre}"