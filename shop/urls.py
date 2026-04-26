from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("categories/", views.categories, name="categories"),
    path("categories/<slug:slug>/", views.category_detail, name="category_detail"),
    path("products/", views.all_products, name="products"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
