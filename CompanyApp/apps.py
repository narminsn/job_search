from django.apps import AppConfig


class CompanyappConfig(AppConfig):
    name = 'CompanyApp'

    def ready(self):
        import CompanyApp.signals
