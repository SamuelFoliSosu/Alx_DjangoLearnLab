from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        # Import your signals here to ensure they are registered
        # import relationship_app.signals # noqa F401
        pass
