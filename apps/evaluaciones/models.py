from django.db import models
from apps.rubricas.models import Rubrica, Criterio, Nivel
from apps.competencias_programa.models import ResultadoAprendizajePrograma
from apps.competencias_asignatura.models import ResultadoAprendizajeAsignatura

class Evaluacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)

    # Puede evaluar un RA de programa o un RA de asignatura
    resultado_aprendizaje_programa = models.ForeignKey(
        ResultadoAprendizajePrograma,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='evaluaciones_programa'
    )

    resultado_aprendizaje_asignatura = models.ForeignKey(
        ResultadoAprendizajeAsignatura,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='evaluaciones_asignatura'
    )

    rubrica = models.ForeignKey(
        Rubrica,
        on_delete=models.CASCADE,
        related_name='evaluaciones'
    )

    class Meta:
        db_table = 'evaluaciones'

    def __str__(self):
        return f"Evaluación #{self.id} – {self.fecha}"
    

class DetalleEvaluacion(models.Model):
    evaluacion = models.ForeignKey(
        Evaluacion,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    criterio = models.ForeignKey(
        Criterio,
        on_delete=models.CASCADE,
        related_name='detalles_evaluacion'
    )
    nivel = models.ForeignKey(
        Nivel,
        on_delete=models.CASCADE,
        related_name='detalles_evaluacion'
    )
    comentario = models.TextField(blank=True)

    class Meta:
        db_table = 'detalles_evaluacion'

    def __str__(self):
        return f"Detalle (Evaluación #{self.evaluacion.id}, Criterio: {self.criterio.nombre})"

