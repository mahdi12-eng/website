from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("", include("shop.urls")),
]
# hi mahdi how are you today
