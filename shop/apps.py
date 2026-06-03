from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = "shop"

    def ready(self) -> None:  # registering the template tags
        from .templatetags.shop_tags import register
        # from .. import models
