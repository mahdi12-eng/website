from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.utils.text import slugify
from .models import Address, Categories, Customers, Feedbacks, Invoices, Products
from django.core.paginator import Paginator

# TODO: optimize the way products and categories are loaded to avoid unnecessary in-memory data duplication and ensure data consistency with the database

# TODO: Refactor to use Django's ORM more effectively and avoid in-memory data duplication
# TODO: Implement proper error handling and user feedback for actions like adding/removing hot products
# TODO: Consider using Django's class-based views for better organization and maintainability
# TODO: Add pagination for product listings and search results to improve performance with large datasets
# TODO: Implement user authentication and permissions to control access to admin features like managing hot products
# TODO: Optimize database queries to reduce load and improve response times, especially for product and category retrieval
# TODO: Add unit tests to ensure the correctness of views and template tags, especially for edge cases like missing products or categories


ADMIN_CONTROLL = False


def get_products_from_db():
    products_list = []

    for product in Products.objects.all():
        products_list.append(
            {
                "id": product.pr_id,
                "name": product.name,
                "slug": slugify(product.name),
                "category": slugify(product.category.name),
                "price": f"${product.price:,}",
                "description": product.description,
                "image": product.image,
                "hot": True if product.hot == 1 else False,
            }
        )
    return products_list


#  finished populating PRODUCTS list from the database

CATEGORIES = []
PRODUCTS = get_products_from_db()

if len(CATEGORIES) == 0:
    for category in Categories.objects.all():
        CATEGORIES.append(
            {
                "name": category.name,
                "slug": slugify(category.name),
                "description": category.description,
            }
        )


def exite_admin(req):
    global ADMIN_CONTROLL
    ADMIN_CONTROLL = False
    return index(req)


def turn_admin(request):
    global ADMIN_CONTROLL
    ADMIN_CONTROLL = True
    return index(request)


def index(request):
    # products = get_products()
    # Filter out any "bowl" category if mistakenly added
    clean_categories = [
        c
        for c in CATEGORIES
        if "bowl" not in c["name"].lower() and "bowl" not in c["slug"].lower()
    ]
    featured_products = Products.objects.filter(hot=1)
    return render(
        request,
        "shop/index.html",
        {
            "categories": CATEGORIES,
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
        context = {"products": PRODUCTS, "title": "NEW IN & BESTSELLERS"}
    return render(request, "shop/products.html", context)


def category_detail(request, category_name):
    category = Categories.objects.filter(name=category_name.title())
    if not category:
        return render(request, "shop/not_found.html")

    # all_products = get_products()
    category_products = Products.objects.filter(
        category__name=category_name.title())

    # FIX: Remove any "bowl" products mistakenly added to phones
    if category_name == "phones":
        category_products = [
            p
            for p in category_products
            if "bowl" not in p.name.lower() and "bowl" not in str(p.image).lower()
        ]

    return render(
        request,
        "shop/category_detail.html",
        {"category": category, "products": category_products},
    )


# ---------------------- Hot Section -----------------#


def hot_products(request):
    HOT_PRODUCTS = Products.objects.filter(hot=1)  # filtering the hots
    pagi = Paginator(HOT_PRODUCTS, 12)  # setting the page size
    page_no = request.GET.get("p", 2)  # setting the page

    try:
        page_obj = pagi.page(page_no)
    except:
        page_obj = pagi.page(pagi.num_pages)
    return render(
        request, "shop/hot.html", {"products":  page_obj,
                                   "controll": ADMIN_CONTROLL}
    )


def delete_from_hots(req, id):
    global PRODUCTS
    target = Products.objects.get(pr_id=id)
    target.hot = 0
    target.save()
    for product in PRODUCTS:
        if product["hot"] == True and product["id"] == id:
            product["hot"] = False

    return redirect("hot_products")


def product_detail(request, product_name):
    # all_products = get_products()

    ##################### plz explain this why you do this #################
    product = Products.objects.filter(name=product_name)
    if not product:
        return render(request, "shop/not_found.html")

    # Get related products (same category)
    related = Products.objects.filter(
        category__name=product["category"].title())
    # related = [
    #     p
    #     for p in PRODUCTS
    #     if p["category"] == product["category"] and p["slug"] != product_slug
    # ][:4]
    # related = [
    #     p
    print(related)
    return render(
        request, "shop/product_detail.html", {
            "product": product, "related": related}
    )


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")


def login_view(request):
    return render(request, "shop/login.html")


def register_view(request):
    return render(request, "shop/register.html")
