from django.apps import AppConfig


class AcountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "acounts"

    def ready(self):
        pass
        # from .. import models
