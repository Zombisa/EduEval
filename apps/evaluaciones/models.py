from django.db import models

# Aún no hay modelos definidos explícitamente en el archivo SQL original
# Puedes usar esto como placeholder

class EvaluacionPlaceholder(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    class Meta:
        managed = False  # Este modelo no genera tabla real
        verbose_name = "Evaluación (placeholder)"
