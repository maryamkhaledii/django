from django.apps import AppConfig

class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals

