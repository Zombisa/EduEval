from django.db import models
from apps.competencias_programa.models.models import CompetenciaPrograma
from apps.rubricas.models.models import Rubrica

class CompetenciaAsignatura(models.Model):
    programa = models.ForeignKey(
        CompetenciaPrograma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='competencias_asignatura'
    )
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
    rubrica = models.ForeignKey(
    Rubrica,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='resultados_aprendizaje'
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
