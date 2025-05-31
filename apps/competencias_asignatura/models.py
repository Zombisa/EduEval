from django.db import models

class CompetenciaAsignatura(models.Model):
    id_asignatura = models.IntegerField(default=0)
    descripcion = models.TextField()    
    # Nivel: 1 = Básico, 2 = Medio, 3 = Avanzado
    nivel = models.PositiveIntegerField(
        choices=[
            (1, 'Básico'),
            (2, 'Medio'),
            (3, 'Avanzado'),
        ],
        default=1
    )

    def __str__(self):
        return f"Competencia ({self.id_asignatura} - Nivel {self.get_nivel_display()})"

class ResultadoAprendizajeAsignatura(models.Model):
    competencia = models.ForeignKey(
        CompetenciaAsignatura,
        related_name='resultados_aprendizaje',
        on_delete=models.SET_NULL,  # Si se elimina la competencia, desvincula el RA (no lo elimina)
        null=True,
        blank=True
    )
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"RA ({'Sin competencia' if not self.competencia else self.competencia.id}) - {estado}"
