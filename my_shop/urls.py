from django.urls import path, include
from shop.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
import debug_toolbar

sitemaps = {"static": StaticViewSitemap, }
urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {
        "sitemaps": sitemaps}, name="django.contrib.views.sitemap"),
    path("", include(("shop.urls", "shop"), namespace="shop")),
    path(
        "acounts/",
        include("acounts.urls"),
        name="acounts"
    ),

    path("__debug__/", include(debug_toolbar.urls))
]
