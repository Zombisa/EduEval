from django.db import models

class Rubrica(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class NivelDesempeno(models.Model):
    NIVEL_CHOICES = [
        (1, 'Bajo'),
        (2, 'Medio'),
        (3, 'Alto'),
    ]

    nivel = models.PositiveSmallIntegerField(choices=NIVEL_CHOICES)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return dict(self.NIVEL_CHOICES).get(self.nivel, 'Desconocido')


class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE, related_name='criterios')
    descripcion = models.TextField()
    ponderado = models.FloatField(help_text="Ponderación del criterio en la evaluación (0.0 a 1.0)", default=1.0)
    nivel = models.PositiveSmallIntegerField(
        choices=[
            (1, 'Básico'),
            (2, 'Medio'),
            (3, 'Avanzado'),
        ],
        default=1
    )

    def __str__(self):
        return f"Criterio ({self.descripcion[:30]}...)"
