from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.utils.text import slugify
from .models import Address, Categories, Customers, Feedbacks, Invoices, Products
from django.core.paginator import Paginator
from .forms import LoginForm, RegisterForm, CustomersForm
from django.contrib import messages
# TODO: optimize the way products and categories are loaded to avoid unnecessary in-memory data duplication and ensure data consistency with the database

# TODO: Refactor to use Django's ORM more effectively and avoid in-memory data duplication
# TODO: Implement proper error handling and user feedback for actions like adding/removing hot products
# TODO: Consider using Django's class-based views for better organization and maintainability
# TODO: Add pagination for product listings and search results to improve performance with large datasets
# TODO: Implement user authentication and permissions to control access to admin features like managing hot products
# TODO: Optimize database queries to reduce load and improve response times, especially for product and category retrieval
# TODO: Add unit tests to ensure the correctness of views and template tags, especially for edge cases like missing products or categories


ADMIN_CONTROLL = False


#  finished populating PRODUCTS list from the database


def exite_admin(req):
    global ADMIN_CONTROLL
    ADMIN_CONTROLL = False
    return index(req)


def turn_admin(request):
    global ADMIN_CONTROLL
    ADMIN_CONTROLL = True
    return index(request)


def index(request):
    featured_products = Products.objects.filter(hot=1)
    categories = Categories.objects.all()
    return render(
        request,
        "shop/index.html",
        {
            "categories": categories,
            "featured_products": featured_products,
            "controll": ADMIN_CONTROLL,
        },
    )


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
    # all_products = get_products()
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
                                   "controll": ADMIN_CONTROLL}
    )


def delete_from_hots(req, id):
    pass

    # target = Products.objects.get(pr_id=id)
    # target.hot = 0
    # target.save()
    # for product in PRODUCTS:
    #     if product["hot"] == True and product["id"] == id:
    #         product["hot"] = False

    # return redirect("hot_products")


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


def login_view(request):
    if request.method == "POSt":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url(index))
    form = LoginForm()
    return render(request, "shop/login.html")


def register_view(request):
    if request.method == "POST":
        form = CustomersForm(request.POST)
        print("post request")
        if form.is_valid():
            print("form is valid ")
            form.save()
            return redirect(url(index))
    form = CustomersForm(request.POST)
    return render(request, "shop/register.html", {"form": form})
