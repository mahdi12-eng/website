from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return ["shop:home", "shop:categories", "shop:products", "shop:login", "shop:about", "shop:contact", "shop:register"]

    def location(self, item):
        return reverse(item)
