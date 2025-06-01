from django.db import models

class CompetenciaPrograma(models.Model):
    descripcion = models.TextField()
    id_programa = models.IntegerField(default=0)  # ID del programa como campo entero
    nivel = models.PositiveIntegerField(
        choices=[
            (1, 'Básico'),
            (2, 'Medio'),
            (3, 'Avanzado')
        ],
        default=1
    )

    def __str__(self):
        return f"Competencia {self.id} - Programa {self.id_programa}"


class ResultadoAprendizajePrograma(models.Model):
    competencia = models.ForeignKey(
        CompetenciaPrograma,
        related_name='resultados_aprendizaje',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RA Programa {self.id} - Competencia {self.competencia_id}"
