from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import connection
from .models import NivelDesempeno

def table_exists(table_name):
    return table_name in connection.introspection.table_names()

@receiver(post_migrate)
def crear_niveles_predeterminados(sender, **kwargs):
    if not table_exists('rubricas_niveldesempeno'):
        return 

    niveles = [
        (1, "Bajo"),
        (2, "Medio"),
        (3, "Alto"),
    ]

    for nivel, descripcion in niveles:
        NivelDesempeno.objects.get_or_create(nivel=nivel, defaults={'descripcion': descripcion})
