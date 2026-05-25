from django.urls import path, include
from shop.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin

sitemaps = {"static": StaticViewSitemap, }
urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {
        "sitemaps": sitemaps}, name="django.contrib.views.sitemap"),
    path("", include(("shop.urls", "shop"), namespace="shop")),
]
