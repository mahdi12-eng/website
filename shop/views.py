from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Address, Categories, Customers, Feedbacks, Invoices, Products

ADMIN_CONTROLL = False


def get_products_from_db():
    products_list = []

    for product in Products.objects.all():
        products_list.append(
            {
                "id": product.pr_id,
                "name": product.name,
                "slug": slugify(product.name),
                "category": product.category.slug,
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
                "slug": category.slug,
                "description": category.description,
            }
        )


def price_fixe(p):
    return int(p.strip("$").replace(",", ""))


# Helper to get products with slugs
# def get_products():


#     for i, item in enumerate(PRODUCTS):
#         item["id"] = i
#         item["slug"] = slugify(item["name"])
#     return PRODUCTS
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
    featured_products = [p for p in PRODUCTS if p.get("hot")]
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
    query = request.GET.get("q")
    # all_products = get_products()

    if query:
        filtered_products = [
            p
            for p in PRODUCTS
            if query.lower() in p["name"].lower()
            or query.lower() in p["description"].lower()
        ]
        context = {
            "products": filtered_products,
            "query": query,
            "title": f"SEARCH RESULTS FOR '{query}'",
        }
    else:
        context = {"products": PRODUCTS, "title": "NEW IN & BESTSELLERS"}
    return render(request, "shop/products.html", context)


def category_detail(request, category_slug):
    category = next((c for c in CATEGORIES if c["slug"] == category_slug), None)
    if not category:
        return render(request, "shop/not_found.html")

    # all_products = get_products()
    category_products = [p for p in PRODUCTS if p["category"] == category_slug]
    return render(
        request,
        "shop/category_detail.html",
        {"category": category, "products": category_products},
    )


# ---------------------- Hot Section -----------------#


def hot_products(request):
    print(PRODUCTS[0])
    HOT_PRODUCTS = [
        product for product in PRODUCTS if product["hot"]
    ]  # filtering the hots
    return render(
        request, "shop/hot.html", {"products": HOT_PRODUCTS, "controll": ADMIN_CONTROLL}
    )


def delete_from_hots(req, id):
    print(id)
    global PRODUCTS
    target = Products.objects.get(pr_id=id)
    target.hot = 0
    target.save()
    for product in PRODUCTS:
        if product["hot"] == True and product["id"] == id:
            product["hot"] == False

    return hot_products(req)


def product_detail(request, product_slug):
    # all_products = get_products()
    product = next((p for p in PRODUCTS if p["slug"] == product_slug), None)
    if not product:
        return render(request, "shop/not_found.html")

    # Get related products (same category)
    related = [
        p
        for p in PRODUCTS
        if p["category"] == product["category"] and p["slug"] != product_slug
    ][:4]

    return render(
        request, "shop/product_detail.html", {"product": product, "related": related}
    )


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")


def login_view(request):
    return render(request, "shop/login.html")


def register_view(request):
    return render(request, "shop/register.html")
