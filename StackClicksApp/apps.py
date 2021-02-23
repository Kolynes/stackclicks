from django.apps import AppConfig


class StackclicksappConfig(AppConfig):
    name = 'StackClicksApp'

    def ready(self):
        from . import signals