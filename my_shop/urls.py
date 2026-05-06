from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
]
# hi mahdi how are you today
