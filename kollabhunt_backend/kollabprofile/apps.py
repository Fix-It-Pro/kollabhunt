from django.apps import AppConfig

class KollabprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kollabprofile'

    def ready(self):
        import kollabprofile.signals
