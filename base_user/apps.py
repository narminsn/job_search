from django.apps import AppConfig


class BaseUserConfig(AppConfig):
    name = 'base_user'

    def ready(self):
        import base_user.signals
