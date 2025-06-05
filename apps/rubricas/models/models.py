from django.core.exceptions import ValidationError
from django.db import models

class Rubrica(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def clean(self):
        if not self.nombre.strip():
            raise ValidationError("El nombre de la rúbrica no puede estar vacío.")

    def __str__(self):
        return self.nombre

class NivelDesempeno(models.Model):
    nivel = models.PositiveIntegerField(unique=True)
    descripcion = models.CharField(max_length=100, default="Sin descripción")

    def clean(self):
        if not self.descripcion.strip():
            raise ValidationError("La descripción del nivel de desempeño no puede estar vacía.")

    def __str__(self):
        return f"{self.nivel} - {self.descripcion}"

class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, related_name='criterios')
    descripcion = models.TextField()
    ponderado = models.FloatField(default=1.0)
    nivel = models.PositiveSmallIntegerField(
        choices=[(1, 'Básico'), (2, 'Medio'), (3, 'Avanzado')],
        default=1
    )

    def clean(self):
        if not self.descripcion.strip():
            raise ValidationError("La descripción del criterio no puede estar vacía.")
        if not 0.0 <= self.ponderado <= 1.0:
            raise ValidationError("El valor ponderado debe estar entre 0.0 y 1.0.")

    def __str__(self):
        return f"Criterio ({self.descripcion[:30]}...)"
