from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from apps.rubricas.models.models import Rubrica, Criterio
from apps.evaluaciones.models.models import ResultadoEvaluacion
from apps.competencias_asignatura.models.models import CompetenciaAsignatura

class Command(BaseCommand):
    help = "Crea grupos (roles) con permisos y usuarios demo"

    def handle(self, *args, **kwargs):
        roles = {
            "Evaluador": {
                "permisos": [
                    ("view_rubrica", Rubrica),
                    ("view_criterio", Criterio),
                ]
            },
            "Profesor": {
                "permisos": [
                    ("view_resultadoevaluacion", ResultadoEvaluacion),
                    ("change_resultadoevaluacion", ResultadoEvaluacion),
                ]
            },
            "Coordinador": {
                "permisos": [
                    ("add_rubrica", Rubrica), ("change_rubrica", Rubrica), ("delete_rubrica", Rubrica),
                    ("add_criterio", Criterio), ("change_criterio", Criterio),
                    ("add_competenciaasignatura", CompetenciaAsignatura), ("change_competenciaasignatura", CompetenciaAsignatura),
                ]
            }
        }

        for nombre, config in roles.items():
            grupo, _ = Group.objects.get_or_create(name=nombre)
            for codename, modelo in config["permisos"]:
                ct = ContentType.objects.get_for_model(modelo)
                permiso = Permission.objects.get(codename=codename, content_type=ct)
                grupo.permissions.add(permiso)
            self.stdout.write(f"Grupo '{nombre}' creado con permisos asignados.")

        usuarios = [
            ("eva1", "Evaluador"),
            ("profe1", "Profesor"),
            ("coor1", "Coordinador"),
        ]
        for username, rol in usuarios:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password("123456")
                user.save()
            user.groups.set([Group.objects.get(name=rol)])
            self.stdout.write(f"Usuario '{username}' asignado al grupo '{rol}' (password: 123456)")

        self.stdout.write(self.style.SUCCESS("Usuarios y roles creados correctamente."))
