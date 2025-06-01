from django.db import models
from apps.rubricas.models.models import Rubrica, Criterio, NivelDesempeno

class Evaluacion(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, related_name='evaluaciones')
    estudiante = models.CharField(max_length=255, default='desconocido')
    evaluador = models.CharField(max_length=255, default='desconocido')
    fecha = models.DateField(auto_now_add=True)
    retroalimentacion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Evaluación de {self.estudiante} con rúbrica {self.rubrica.id}"

class ResultadoEvaluacion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='resultados')
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    nivel_seleccionado = models.ForeignKey(NivelDesempeno, on_delete=models.SET_NULL, null=True)
    nota = models.FloatField()

    def __str__(self):
        return f"Resultado para criterio {self.criterio.id} en evaluación {self.evaluacion.id}"
