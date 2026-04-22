from django.contrib import admin
from django.urls import path, include
from shop import views  # This tells Django to look at your shop logic

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("shop.urls")
    ),  # this tell to Django if any requested to this address redirect it to this file
]
