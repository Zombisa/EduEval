from django.db import models
from apps.competencias_asignatura.models.models import ResultadoAprendizajeAsignatura

class Rubrica(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    resultado_aprendizaje = models.ForeignKey(
        ResultadoAprendizajeAsignatura,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rubricas'
    )

    def __str__(self):
        return self.nombre


class NivelDesempeno(models.Model):
    nivel = models.PositiveIntegerField(unique=True)
    descripcion = models.CharField(max_length=100, default="Sin descripción") 

    def __str__(self):
        return f"{self.get_nivel_display()} - {self.descripcion}"


class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, related_name='criterios')
    descripcion = models.TextField()
    ponderado = models.FloatField(help_text="Ponderación del criterio en la evaluación (0.0 a 1.0)", default=1.0)
    nivel = models.PositiveSmallIntegerField(
        choices=[
            (1, 'Básico'),
            (2, 'Medio'),
            (3, 'Avanzado'),
        ],
        default=1
    )

    def __str__(self):
        return f"Criterio ({self.descripcion[:30]}...)"
