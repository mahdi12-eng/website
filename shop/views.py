from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Address, Categories, Customers, Feedbacks, Invoices, Products

PRODUCTS = [
    # --- LAPTOPS (16 items) ---
    {
        "name": "Dell Precision 5570",
        "category": "laptops",
        "price": "$1,450",
        "description": "Powerful workstation for high-end professional tasks.",
        "image": " 5570computer.jpg",
        "hot": True,
    },
    {
        "name": "MacBook Pro M3 Max",
        "category": "laptops",
        "price": "$2,499",
        "description": "The ultimate power for developers and creators.",
        "image": " macbookcomputer.jpg",
        "hot": True,
    },
    {
        "name": "MacBook Air 13-inch",
        "category": "laptops",
        "price": "$1,099",
        "description": "Thin, light, and faster than ever.",
        "image": " mscbook1.jpg",
        "hot": True,
    },
    {
        "name": "Dell Latitude 7420",
        "category": "laptops",
        "price": "$899",
        "description": "Compact business laptop with great battery life.",
        "image": " computer.jpg",
    },
    {
        "name": "Precision Workstation 5540",
        "category": "laptops",
        "price": "$1,150",
        "description": "Reliable performance in a sleek design.",
        "image": " computer5540.webp",
        "hot": True,
    },
    {
        "name": "MacBook Pro Silver",
        "category": "laptops",
        "price": "$1,299",
        "description": "Classic design with modern internals.",
        "image": " macbook3.jpg",
    },
    {
        "name": "Dell XPS 15",
        "category": "laptops",
        "price": "$1,350",
        "description": "Stunning display with powerful performance.",
        "image": " computer1.jpg",
    },
    {
        "name": "Workstation Pro 0",
        "category": "laptops",
        "price": "$950",
        "description": "Budget friendly professional laptop.",
        "image": " computer0.jpg",
    },
    {
        "name": "Workstation Pro 00",
        "category": "laptops",
        "price": "$1,050",
        "description": "Reliable daily driver for work.",
        "image": " computer00.jpg",
    },
    {
        "name": "Dell Precision V2",
        "category": "laptops",
        "price": "$1,400",
        "description": "High-end graphics and CPU power.",
        "image": " computer2.jpg",
    },
    {
        "name": "MacBook Pro M2",
        "category": "laptops",
        "price": "$1,599",
        "description": "Fast and efficient Apple Silicon.",
        "image": " macbook4.jpg",
    },
    {
        "name": "MacBook Pro Space Gray",
        "category": "laptops",
        "price": "$1,799",
        "description": "The choice for professional editors.",
        "image": " macbook5.jpg",
    },
    {
        "name": "MacBook Pro 16",
        "category": "laptops",
        "price": "$2,199",
        "description": "Large screen for maximum productivity.",
        "image": " macbook6.jpg",
    },
    {
        "name": "Precision Elite",
        "category": "laptops",
        "price": "$1,850",
        "description": "Top tier Dell workstation performance.",
        "image": " precisioncomputer.webp",
    },
    # --- PHONES (21 items) ---
    {
        "name": "iPhone 17 Pro Max",
        "category": "phones",
        "price": "$1,299",
        "description": "The next generation of intelligence and speed.",
        "image": " iphone17.jpg",
        "hot": True,
    },
    {
        "name": "Samsung Galaxy S26 Ultra",
        "category": "phones",
        "price": "$1,399",
        "description": "The peak of mobile photography and power.",
        "image": " s26ultra.jpg",
        "hot": True,
    },
    {
        "name": "iPhone 16 Gold",
        "category": "phones",
        "price": "$999",
        "description": "Elegance meets performance.",
        "image": " iphone.webp",
        "hot": True,
    },
    {
        "name": "Samsung Note 23 Plus",
        "category": "phones",
        "price": "$950",
        "description": "Designed for productivity with S-Pen support.",
        "image": " notephone23.jpg",
        "hot": True,
    },
    {
        "name": "Infinix Zero Pro",
        "category": "phones",
        "price": "$450",
        "description": "Premium features at an accessible price point.",
        "image": " nfnxmobile.jpg",
    },
    {
        "name": "Samsung S26 FE",
        "category": "phones",
        "price": "$799",
        "description": "Fan favorite features in a new design.",
        "image": " s26.jpg",
    },
    {
        "name": "iPhone 17 Base",
        "category": "phones",
        "price": "$899",
        "description": "Simple, powerful, and beautiful.",
        "image": " iphone177.jpg",
    },
    {
        "name": "iPhone 15 Colors",
        "category": "phones",
        "price": "$799",
        "description": "Available in multiple vibrant colors.",
        "image": " iphone-15-colors-1.webp",
    },
    {
        "name": "Classic iPhone",
        "category": "phones",
        "price": "$599",
        "description": "Reliable and familiar iOS experience.",
        "image": " iphone.jpg",
    },
    {
        "name": "iPhone Pro Edition",
        "category": "phones",
        "price": "$1,099",
        "description": "Professional grade mobile camera.",
        "image": " iphone.png",
    },
    {
        "name": "iPhone 16 Girl Edition",
        "category": "phones",
        "price": "$999",
        "description": "Special edition for fashion lovers.",
        "image": " iphone16girl.jpg",
    },
    {
        "name": "iPhone Handheld",
        "category": "phones",
        "price": "$850",
        "description": "Compact design for one-hand use.",
        "image": " iphonehand.jpg",
    },
    {
        "name": "iPhone Handheld V2",
        "category": "phones",
        "price": "$899",
        "description": "Improved grip and battery life.",
        "image": " iphonehand2.jpg",
    },
    {
        "name": "Note Phone Classic",
        "category": "phones",
        "price": "$750",
        "description": "Large display for media consumption.",
        "image": " notephone.jpg",
    },
    {
        "name": "Mobile Pro 43",
        "category": "phones",
        "price": "$400",
        "description": "Solid mid-range performance.",
        "image": " phone43.jpg",
    },
    {
        "name": "Phone of Beauty",
        "category": "phones",
        "price": "$1,150",
        "description": "Exquisite design and screen.",
        "image": " phoneofbeauty.jpg",
    },
    {
        "name": "Phone of S",
        "category": "phones",
        "price": "$950",
        "description": "Speed and simplicity combined.",
        "image": " phoneofs.jpg",
    },
    {
        "name": "Phone S26 Pro",
        "category": "phones",
        "price": "$1,250",
        "description": "High-end specs for power users.",
        "image": " phones26.jpg",
    },
    {
        "name": "Samsung Mobile Elite",
        "category": "phones",
        "price": "$1,100",
        "description": "Premium Samsung build quality.",
        "image": " samsungmobile.jpg",
    },
    {
        "name": "S-Model Phone",
        "category": "phones",
        "price": "$850",
        "description": "Stylish and modern smartphone.",
        "image": " smodelphone.jpg",
    },
    {
        "name": "Generic Smart Phone",
        "category": "phones",
        "price": "$300",
        "description": "All essential features included.",
        "image": " images.jpg",
    },
    # --- AFGHANI CLOTHES (20 items) ---
    {
        "name": "Royal Afghani Gand",
        "category": "afghani-clothes",
        "price": "$180",
        "description": "Exquisite hand-embroidered traditional luxury dress.",
        "image": " gand.jpg",
        "hot": True,
    },
    {
        "name": "Hazaragi Cultural Dress",
        "category": "afghani-clothes",
        "price": "$110",
        "description": "Vibrant traditional Hazaragi attire.",
        "image": " hazaragiclothes.jpg",
        "hot": True,
    },
    {
        "name": "Silk Embroidered Gand",
        "category": "afghani-clothes",
        "price": "$140",
        "description": "Soft silk with intricate needlework.",
        "image": " gand1.jpg",
        "hot": True,
    },
    {
        "name": "Kandahari Khamak Gand",
        "category": "afghani-clothes",
        "price": "$160",
        "description": "Famous Kandahari hand-stitched embroidery.",
        "image": " gand3.jpg",
        "hot": True,
    },
    {
        "name": "Afghan Party Wear",
        "category": "afghani-clothes",
        "price": "$130",
        "description": "Modern twist on traditional Afghan fashion.",
        "image": " girlcloth.jpg",
    },
    {
        "name": "Hazaragi Party Set",
        "category": "afghani-clothes",
        "price": "$125",
        "description": "Perfect for weddings and special occasions.",
        "image": " hazaragicllothes2.jpg",
    },
    {
        "name": "Traditional Velvet Gand",
        "category": "afghani-clothes",
        "price": "$155",
        "description": "Deep red velvet with gold embroidery.",
        "image": " gand5.jpg",
    },
    {
        "name": "Special Edition Gand",
        "category": "afghani-clothes",
        "price": "$200",
        "description": "Premium hand-made cultural attire.",
        "image": " 671704370_122109552285122650_4200145947817601766_n.jpg",
    },
    {
        "name": "Kochi Style Gand",
        "category": "afghani-clothes",
        "price": "$145",
        "description": "Traditional Kochi tribal embroidery.",
        "image": " gand2.jpg",
    },
    {
        "name": "Silk Party Gand",
        "category": "afghani-clothes",
        "price": "$135",
        "description": "Elegant silk dress for celebrations.",
        "image": " gand4.jpg",
    },
    {
        "name": "Classic Chapan",
        "category": "afghani-clothes",
        "price": "$95",
        "description": "Traditional Afghan outer garment.",
        "image": " gand6.jpg",
    },
    {
        "name": "Royal Chapan",
        "category": "afghani-clothes",
        "price": "$120",
        "description": "High quality velvet chapan.",
        "image": " gand8.jpg",
    },
    {
        "name": "Afghan Girl Cloth",
        "category": "afghani-clothes",
        "price": "$85",
        "description": "Beautiful dress for young girls.",
        "image": " girlcloth3.jpg",
    },
    {
        "name": "Velvet Girl Dress",
        "category": "afghani-clothes",
        "price": "$90",
        "description": "Soft velvet dress with patterns.",
        "image": " girlclothes5.jpg",
    },
    {
        "name": "Modern Gand V7",
        "category": "afghani-clothes",
        "price": "$165",
        "description": "Newest design in our cultural collection.",
        "image": " gnad7.jpg",
    },
    {
        "name": "Hazaragi Cultural V3",
        "category": "afghani-clothes",
        "price": "$115",
        "description": "Authentic Hazaragi embroidery.",
        "image": " hazaragiclothes3.jpg",
    },
    {
        "name": "Hazaragi Cultural V4",
        "category": "afghani-clothes",
        "price": "$120",
        "description": "Intricate hand-made patterns.",
        "image": " hazaragiclothes4.jpg",
    },
    {
        "name": "Traditional Hazar Clothes",
        "category": "afghani-clothes",
        "price": "$105",
        "description": "Classic Hazaragi style attire.",
        "image": " hazarclothes.jpg",
    },
    {
        "name": "Cultural Chapan Cao",
        "category": "afghani-clothes",
        "price": "$110",
        "description": "Unique regional style chapan.",
        "image": " cao.png",
    },
    # --- HOME & KITCHEN (13 items) ---
    {
        "name": "Istalif Ceramic Bowl",
        "category": "home-kitchen",
        "price": "$55",
        "description": "Authentic turquoise-glazed pottery from Istalif.",
        "image": " istalif.jpg",
        "hot": True,
    },
    {
        "name": "Traditional Afghan Teapot",
        "category": "home-kitchen",
        "price": "$40",
        "description": "Classic design for serving green tea.",
        "image": " teapot.jpg",
    },
    {
        "name": "Copper Cooking Boiler",
        "category": "home-kitchen",
        "price": "$85",
        "description": "Hand-hammered copper for authentic cooking.",
        "image": " boiler.jpg",
    },
    {
        "name": "Engraved Kitchen Pot",
        "category": "home-kitchen",
        "price": "$65",
        "description": "Beautifully engraved serving pot.",
        "image": " pot94.jpg",
    },
    {
        "name": "Afghan Ceramic Bowl Set",
        "category": "home-kitchen",
        "price": "$45",
        "description": "Hand-painted ceramic bowls for your table.",
        "image": " bowl.jpg",
    },
    {
        "name": "Ceramic Tea Pot 00",
        "category": "home-kitchen",
        "price": "$35",
        "description": "Elegant white ceramic teapot with traditional patterns.",
        "image": " teapot00.jpg",
    },
    {
        "name": "Blue Istalif Bowl",
        "category": "home-kitchen",
        "price": "$50",
        "description": "Deep blue glazed ceramic bowl.",
        "image": " boel.jpg",
    },
    {
        "name": "Large Cooking Boiler",
        "category": "home-kitchen",
        "price": "$95",
        "description": "Large capacity copper boiler.",
        "image": " boiler45.jpg",
    },
    {
        "name": "Small Ceramic Bowl",
        "category": "home-kitchen",
        "price": "$25",
        "description": "Perfect for sides and sauces.",
        "image": " bowel.jpg",
    },
    {
        "name": "Patterned Bowl 34",
        "category": "home-kitchen",
        "price": "$30",
        "description": "Beautifully patterned serving bowl.",
        "image": "bowl34.jpg",
    },
    {
        "name": "Modern Ceramic Bowl",
        "category": "home-kitchen",
        "price": "$40",
        "description": "Sleek modern ceramic design.",
        "image": "bowl44.webp",
    },
    {
        "name": "Bowliton Special",
        "category": "home-kitchen",
        "price": "$60",
        "description": "Limited edition kitchen bowl.",
        "image": "bowliton.webp",
    },
    {
        "name": "Traditional Teapot 5",
        "category": "home-kitchen",
        "price": "$45",
        "description": "Classic Afghan tea set piece.",
        "image": "teapot5.jpg",
    },
    {
        "name": "Kitchen Poy",
        "category": "home-kitchen",
        "price": "$50",
        "description": "Handcrafted kitchen essential.",
        "image": "poy.webp",
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
        "name": "Afghani Clothes",
        "description": "Traditional gand, chapan, and ceremony clothing styles.",
    },
    {
        "slug": "home-kitchen",
        "name": "Home and Kitchen",
        "description": "Pots, dishes, tea sets, and Afghan home essentials.",
    },
]


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
