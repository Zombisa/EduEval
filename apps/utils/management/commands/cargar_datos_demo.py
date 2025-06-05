from django.core.management.base import BaseCommand
from django.db import transaction, connection
from apps.competencias_programa.models.models import CompetenciaPrograma, ResultadoAprendizajePrograma
from apps.competencias_asignatura.models.models import CompetenciaAsignatura, ResultadoAprendizajeAsignatura
from apps.rubricas.models.models import Rubrica, Criterio, NivelDesempeno

def reiniciar_autoincremento(nombre_tabla):
    with connection.cursor() as cursor:
        cursor.execute(f"ALTER TABLE {nombre_tabla} AUTO_INCREMENT = 1")

class Command(BaseCommand):
    help = "Carga datos demo: programas, competencias, RA y rúbricas con criterios."

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write("Borrando datos anteriores...")

            Criterio.objects.all().delete()
            Rubrica.objects.all().delete()
            ResultadoAprendizajeAsignatura.objects.all().delete()
            CompetenciaAsignatura.objects.all().delete()
            ResultadoAprendizajePrograma.objects.all().delete()
            CompetenciaPrograma.objects.all().delete()

            for tabla in [
                'rubricas_criterio',
                'rubricas_rubrica',
                'competencias_asignatura_resultadoaprendizajeasignatura',
                'competencias_asignatura_competenciaasignatura',
                'competencias_programa_resultadoaprendizajeprograma',
                'competencias_programa_competenciaprograma',
            ]:
                reiniciar_autoincremento(tabla)

            self.stdout.write("Cargando niveles de desempeño...")
            for i, nombre in [(1, "Básico"), (2, "Medio"), (3, "Avanzado")]:
                NivelDesempeno.objects.get_or_create(nivel=i, defaults={"descripcion": nombre})

            self.stdout.write("Creando competencias de programa y RA...")
            programas = [
                ("Pensamiento crítico", 101),
                ("Comunicación científica", 102),
            ]
            competencias_programa = []
            for desc, id_prog in programas:
                cp = CompetenciaPrograma.objects.create(
                    id_programa=id_prog,
                    descripcion=f"Competencia de {desc}",
                    nivel=2
                )
                competencias_programa.append(cp)
                ResultadoAprendizajePrograma.objects.create(
                    competencia=cp,
                    descripcion=f"Desarrolla habilidades en {desc.lower()}"
                )

            self.stdout.write("Creando competencias de asignatura, rúbricas y RA...")
            asignaturas = [
                (2024, "Bioquímica avanzada"),
                (2025, "Microbiología aplicada"),
            ]
            for idx, (id_asig, desc) in enumerate(asignaturas):
                ca = CompetenciaAsignatura.objects.create(
                    id_asignatura=id_asig,
                    descripcion=f"Competencia asignatura: {desc}",
                    nivel=(idx % 3) + 1,
                    programa=competencias_programa[idx]
                )

                rubrica = Rubrica.objects.create(
                    nombre=f"Rúbrica-{id_asig}",
                    descripcion=f"Rúbrica para evaluar {desc.lower()}"
                )

                for j, criterio in enumerate([
                    "Claridad en el enfoque",
                    "Dominio del tema",
                    "Justificación de argumentos"
                ]):
                    Criterio.objects.create(
                        rubrica=rubrica,
                        descripcion=criterio,
                        ponderado=round(1 / 3, 2),
                        nivel=((j + 1) % 3) + 1
                    )

                ResultadoAprendizajeAsignatura.objects.create(
                    competencia=ca,
                    descripcion=f"RA-{id_asig}: Aplica conocimientos en {desc.lower()}",
                    rubrica=rubrica
                )

            self.stdout.write(self.style.SUCCESS("Datos demo cargados correctamente."))
