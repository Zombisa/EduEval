from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import NivelDesempeno

@receiver(post_migrate)
def crear_niveles_predeterminados(sender, **kwargs):
    niveles = [
        (1, "Bajo"),
        (2, "Medio"),
        (3, "Alto"),
    ]

    for nivel, descripcion in niveles:
        NivelDesempeno.objects.get_or_create(nivel=nivel, defaults={'descripcion': descripcion})
