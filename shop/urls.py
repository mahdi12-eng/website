from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path(
        "categories/", views.index, name="categories"
    ),  # Categories redirects to home/index as we have categories on home
    path(
        "categories/<slug:category_slug>/",
        views.category_detail,
        name="category_detail",
    ),
    path("products/", views.products, name="products"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("hot/", views.hot_products, name="hot_products"),
    path("hot/unhot/<id>", views.delete_from_hots, name="unhot"),
    path("product/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("admin-controll/", views.turn_admin),
    path("admin-exite/", views.exite_admin),
]
