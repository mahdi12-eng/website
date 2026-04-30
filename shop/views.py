from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Address, Categories, Customers, Feedbacks, Invoices, Products

PRODUCTS = [
    # --- LAPTOPS (16 items) ---
]
if len(PRODUCTS) == 0:
    for product in Products.objects.all():
        PRODUCTS.append(
            {
                "name": product.name,
                "category": product.category.slug,
                "price": f"{product.price:,}",
                "description": product.description,
                "image": product.image,
                "hot": True,  # Mark all as hot for demo
            }
        )
#  finished populating PRODUCTS list from the database

CATEGORIES = []

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


for product in PRODUCTS:
    Products.objects.create(
        name=product["name"],
        category=Categories.objects.get(slug=product["category"]),
        price=price_fixe(product["price"]),
        description=product["description"],
        image=product["image"].strip(),
    )


# Helper to get products with slugs
def get_products():
    for i, item in enumerate(PRODUCTS):
        item["id"] = i
        item["slug"] = slugify(item["name"])
    return PRODUCTS


def index(request):
    products = get_products()
    featured_products = [p for p in products if p.get("hot")]
    return render(
        request,
        "shop/index.html",
        {"categories": CATEGORIES, "featured_products": featured_products},
    )


def products(request):
    query = request.GET.get("q")
    all_products = get_products()

    if query:
        filtered_products = [
            p
            for p in all_products
            if query.lower() in p["name"].lower()
            or query.lower() in p["description"].lower()
        ]
        context = {
            "products": filtered_products,
            "query": query,
            "title": f"SEARCH RESULTS FOR '{query}'",
        }
    else:
        context = {"products": all_products, "title": "NEW IN & BESTSELLERS"}
    return render(request, "shop/products.html", context)


def category_detail(request, category_slug):
    category = next((c for c in CATEGORIES if c["slug"] == category_slug), None)
    if not category:
        return render(request, "shop/not_found.html")

    all_products = get_products()
    category_products = [p for p in all_products if p["category"] == category_slug]
    return render(
        request,
        "shop/category_detail.html",
        {"category": category, "products": category_products},
    )


def hot_products(request):
    all_products = get_products()
    hot_items = [item for item in all_products if item.get("hot")]
    return render(request, "shop/hot.html", {"products": hot_items})


def product_detail(request, product_slug):
    all_products = get_products()
    product = next((p for p in all_products if p["slug"] == product_slug), None)
    if not product:
        return render(request, "shop/not_found.html")

    # Get related products (same category)
    related = [
        p
        for p in all_products
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
