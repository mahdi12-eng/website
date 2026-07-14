from django.urls import path
from . import views


app_name = "shop"

urlpatterns = [
    # ------------------ Products section -----------------#
    # path("", views.index, name="home"),
    path("", views.IndexView.as_view(), name="home"),
    path(
        "categories/", views.IndexView.as_view(), name="categories"
    ),  # Categories redirects to home/index as we have categories on home
    path(
        "categories/<int:id>/",
        views.ProductsByCategory.as_view(),
        name="category_detail",
    ),
    # path(
    #     "categories/<int:id>/",
    #     views.category_detail,
    #     name="category_detail",
    # ),
    path("products/", views.products, name="products"),
    # path("hot/", views.hot_products, name="hot_products"),
    path("hot/", views.HotsListView.as_view(), name="hot_products"),
    path("unhot/<int:id>", views.delete_from_hots, name="unhot"),
    path("product/<int:id>/", views.product_detail, name="product_detail"),
    # ---------------- customers section --------------------#
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("add-product/", views.AddProduct.as_view(), name="add-product"),
    path("update-product/<int:pk>", views.ProductUpdateView.as_view(), name="update-product"),
    path("delete-product/<int:pk>", views.ProductsDeleteView.as_view(), name="delete-product"),


]
