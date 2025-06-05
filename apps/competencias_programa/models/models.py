from django.core.exceptions import ValidationError
from django.db import models

class CompetenciaPrograma(models.Model):
    descripcion = models.TextField()
    id_programa = models.IntegerField(default=0)
    nivel = models.PositiveIntegerField(choices=[(1, 'Básico'), (2, 'Medio'), (3, 'Avanzado')], default=1)

    def clean(self):
        if self.id_programa <= 0:
            raise ValidationError("El ID del programa debe ser un número positivo.")
        if not self.descripcion.strip():
            raise ValidationError("La descripción no puede estar vacía.")

    def __str__(self):
        return f"Competencia {self.id} - Programa {self.id_programa}"

class ResultadoAprendizajePrograma(models.Model):
    competencia = models.ForeignKey(CompetenciaPrograma, related_name='resultados_aprendizaje', on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.descripcion.strip():
            raise ValidationError("La descripción del resultado de aprendizaje no puede estar vacía.")

    def __str__(self):
        return f"RA Programa {self.id} - Competencia {self.competencia_id}"
