from django.db import models

class CompetenciaPrograma(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class ResultadoAprendizajePrograma(models.Model):
    competencia = models.OneToOneField(
        CompetenciaPrograma,
        on_delete=models.CASCADE,
        related_name='resultado_aprendizaje'
    )
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RA de {self.competencia.nombre}"
