from django.shortcuts import render


PRODUCTS = [
    {
        "name": "Gaming Laptop Pro 15",
        "category": "laptops",
        "price": "$1,150",
        "description": "High performance laptop for study, work, and gaming.",
    },
    {
        "name": "SlimBook Air 14",
        "category": "laptops",
        "price": "$890",
        "description": "Lightweight laptop with long battery life.",
    },
    {
        "name": "SmartPhone X12",
        "category": "phones",
        "price": "$720",
        "description": "Modern smartphone with fast camera and smooth display.",
    },
    {
        "name": "SmartPhone Lite 9",
        "category": "phones",
        "price": "$390",
        "description": "Affordable phone for everyday communication.",
    },
    {
        "name": "Afghani Gand Classic",
        "category": "afghani-clothes",
        "price": "$65",
        "description": "Traditional Afghan outfit with comfortable fabric.",
    },
    {
        "name": "Afghani Gand Premium",
        "category": "afghani-clothes",
        "price": "$120",
        "description": "Elegant Afghan clothing for special events.",
    },
]


CATEGORIES = [
    {
        "slug": "laptops",
        "name": "Laptops",
        "description": "Powerful laptops for students, professionals, and gamers.",
    },
    {
        "slug": "phones",
        "name": "Phones",
        "description": "Reliable smartphones in different price ranges.",
    },
    {
        "slug": "afghani-clothes",
        "name": "Afghani Gand",
        "description": "Traditional Afghan clothing collection.",
    },
]


def home(request):
    featured_products = PRODUCTS[:3]
    return render(
        request,
        "shop/index.html",
        {"featured_products": featured_products, "categories": CATEGORIES},
    )


def categories(request):
    return render(request, "shop/categories.html", {"categories": CATEGORIES})


def category_detail(request, slug):
    category = next((item for item in CATEGORIES if item["slug"] == slug), None)
    if category is None:
        return render(request, "shop/not_found.html", status=404)

    products = [item for item in PRODUCTS if item["category"] == slug]
    return render(
        request,
        "shop/category_detail.html",
        {"category": category, "products": products},
    )


def all_products(request):
    return render(
        request,
        "shop/products.html",
        {"products": PRODUCTS, "categories": CATEGORIES},
    )


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, "shop/contact.html")
