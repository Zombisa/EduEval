from django.apps import AppConfig


class RubricasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.rubricas'

    def ready(self):
        import apps.rubricas.models.signals
