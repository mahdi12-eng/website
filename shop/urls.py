from django.contrib import admin
from django.urls import path
from . import views  # its import a file current module

urlpatterns = [
    path("", views.home),
]
