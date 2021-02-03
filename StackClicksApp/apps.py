from django.apps import AppConfig


class StackclickappConfig(AppConfig):
    name = 'StackClickApp'

    def ready():
        from . import signals