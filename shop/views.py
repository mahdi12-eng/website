from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.utils.text import slugify
from .models import Address, Categories, Customers, Feedbacks, Invoices, Products
from django.core.paginator import Paginator
# from .forms import LoginForm, RegisterForm, CustomersForm
from django.contrib import messages
# TODO: optimize the way products and categories are loaded to avoid unnecessary in-memory data duplication and ensure data consistency with the database

# TODO: Refactor to use Django's ORM more effectively and avoid in-memory data duplication
# TODO: Implement proper error handling and user feedback for actions like adding/removing hot products
# TODO: Consider using Django's class-based views for better organization and maintainability
# TODO: Add pagination for product listings and search results to improve performance with large datasets
# TODO: Implement user authentication and permissions to control access to admin features like managing hot products
# TODO: Optimize database queries to reduce load and improve response times, especially for product and category retrieval
# TODO: Add unit tests to ensure the correctness of views and template tags, especially for edge cases like missing products or categories


#  finished populating PRODUCTS list from the database

def index(request):
    featured_products = Products.objects.filter(hot=1)
    categories = Categories.objects.all()
    return render(
        request,
        "shop/index.html",
        {
            "categories": categories,
            "featured_products": featured_products,
        },
    )

# TODO :fix this


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


# ---------------------- Hot Section -----------------#


def hot_products(request):
    HOT_PRODUCTS = Products.objects.filter(hot=1)  # filtering the hots
    paginator = Paginator(HOT_PRODUCTS, 12)  # setting the page size
    page_no = request.GET.get("p", 1)  # setting the page
    try:
        page_obj = paginator.get_page(page_no)
    except:
        page_obj = paginator.get_page(1)
    return render(
        request, "shop/hot.html", {"products":  page_obj,
                                   }
    )


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


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")
