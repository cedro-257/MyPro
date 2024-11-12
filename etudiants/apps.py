from django.apps import AppConfig
from . import models


class EtudiantsConfig(AppConfig):
     default_auto_field = 'django.db.models.BigAutoField'
    name = 'etudiants'
