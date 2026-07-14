from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from .models import *


# def index(request):
#     featured_products = Products.objects.filter(hot=1)
#     categories = Categories.objects.all()
#     return render(
#         request,
#         "shop/index.html",
#         {
#             "categories": categories,
#             "featured_products": featured_products,
#         },
#     )

class IndexView(ListView):
    model = Products
    template_name = "shop/index.html"
    context_object_name = "featured_products"
    paginate_by = 9

    def get_queryset(self):
        product = Products.objects.filter(hot=1)
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        return context


def products(request):
    if query := request.GET.get("q"):
        filtered_products = Products.objects.filter(name=query.lower())
        context = {
            "products": filtered_products,
            "query": query,
            "title": f"SEARCH RESULTS FOR '{query}'",
        }
    else:
        all_products = Products.objects.all()
        context = {"products": all_products, "title": "NEW IN & BESTSELLERS"}
    return render(request, "shop/products.html", context)


class ProductsListView(ListView):
    model = Products
    template_name = "shop/products.html"
    context_object_name = "todoes"
    paginate_by = 9

    def get_queryset(self, request):
        if query := request.GET.get("q"):
            products = Products.objects.filter(name=query.lower())
        else:
            products = Products.objects.all()
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "NEW IN & BESTSELLERS"
        return context


def category_detail(request, id):
    category = Categories.objects.get(ct_id=id)
    if not category:
        return render(request, "shop/not_found.html")
    category_products = Products.objects.filter(category=id)
    return render(
        request,
        "shop/category_detail.html",
        {"category": category, "products": category_products},
    )


class ProductsByCategory(ListView):
    model = Products
    template_name = "shop/category_detail.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self, id):
        self.product = Products.objects.filter(category__ct_id=id)
        return self.product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.product[0].category
        return context


# ---------------------- Hot Section -----------------#


# def hot_products(request):
#     HOT_PRODUCTS = Products.objects.filter(hot=1)  # filtering the hots
#     paginator = Paginator(HOT_PRODUCTS, 12)  # setting the page size
#     page_no = request.GET.get("p", 1)  # setting the page
#     try:
#         page_obj = paginator.get_page(page_no)
#     except:
#         page_obj = paginator.get_page(1)
#     return render(
#         request, "shop/hot.html", {"products":  page_obj,
#                                    }
#     )
class HotsListView(ListView):
    model = Products
    template_name = "shop/hot.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        product = Products.objects.filter(hot=1)
        return product


def delete_from_hots(req, id):
    target = Products.objects.get(pr_id=id)
    target.hot = 0
    target.save()

    return redirect(reverse("shop:hot_products"))


def product_detail(request, id):
    product = Products.objects.get(pr_id=id)
    if not product:
        return render(request, "shop/not_found.html")
    # Get related products (same category)
    related = Products.objects.filter(
        category=product.category)

    return render(
        request, "shop/product_detail.html", {
            "product": product, "related": related}
    )


class ProductDetailView(DetailView):
    model = Products
    template_name = "shop/product_detail.html"


class AddProduct(CreateView, LoginRequiredMixin):
    model = Products
    template_name = "shop/add_form.html"
    fields = ["name", "category", "price",
              "description", "image", "amount_in_stock", "hot"]
    success_url = "/"


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Products
    template_name = "shop/add_form.html"
    fields = ["name", "category", "price",
              "description", "image", "amount_in_stock", "hot"]
    success_url = "/"


class ProductsDeleteView(DeleteView, LoginRequiredMixin):
    model = Products
    template_name = "shop/add_form.html"
    success_url = "/"


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")
