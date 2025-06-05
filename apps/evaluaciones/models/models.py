from django.core.exceptions import ValidationError
from django.db import models
from apps.rubricas.models.models import Rubrica, Criterio, NivelDesempeno

class Evaluacion(models.Model):
    rubrica = models.ForeignKey('rubricas.Rubrica', on_delete=models.CASCADE, related_name='evaluaciones')
    estudiante = models.CharField(max_length=255, default='desconocido')
    evaluador = models.CharField(max_length=255, default='desconocido')
    fecha = models.DateField(auto_now_add=True)
    retroalimentacion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def clean(self):
        if not self.estudiante.strip():
            raise ValidationError("El campo 'estudiante' no puede estar vacío.")
        if not self.evaluador.strip():
            raise ValidationError("El campo 'evaluador' no puede estar vacío.")

    def __str__(self):
        return f"Evaluación de {self.estudiante} con rúbrica {self.rubrica.id}"

class ResultadoEvaluacion(models.Model):
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE, related_name='resultados')
    criterio = models.ForeignKey('rubricas.Criterio', on_delete=models.CASCADE)
    nivel_seleccionado = models.ForeignKey('rubricas.NivelDesempeno', on_delete=models.SET_NULL, null=True)
    nota = models.FloatField()

    def clean(self):
        if self.nota < 0 or self.nota > 5:
            raise ValidationError("La nota debe estar entre 0 y 5.")

    def __str__(self):
        return f"Resultado para criterio {self.criterio.id} en evaluación {self.evaluacion.id}"
