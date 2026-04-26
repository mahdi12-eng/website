from django.shortcuts import render


PRODUCTS = [
    {
        "name": "MacBook Air M2 13 - Silver",
        "category": "laptops",
        "price": "$1,099",
        "description": "Apple M2 chip, 8GB RAM, 256GB SSD in Silver finish.",
        "image": "/static/shop/images/products/macbook-air-m2-silver.jpg",
    },
    {
        "name": "MacBook Air M2 13 - Midnight",
        "category": "laptops",
        "price": "$1,149",
        "description": "Apple M2 chip, 8GB RAM, 512GB SSD in Midnight color.",
        "image": "/static/shop/images/products/macbook-air-m2-midnight.jpg",
    },
    {
        "name": "MacBook Pro M3 14 - Space Black",
        "category": "laptops",
        "price": "$1,999",
        "description": "Pro M3 performance with 16GB RAM and 512GB SSD.",
        "image": "/static/shop/images/products/macbook-pro-m3-spaceblack.jpg",
    },
    {
        "name": "MacBook Pro M3 14 - Silver",
        "category": "laptops",
        "price": "$1,949",
        "description": "High-end MacBook Pro for editing, coding, and design.",
        "image": "/static/shop/images/products/macbook-pro-m3-silver.jpg",
    },
    {
        "name": "Dell XPS 13 - Silver",
        "category": "laptops",
        "price": "$1,299",
        "description": "Premium ultrabook with thin bezels and light body.",
        "image": "/static/shop/images/products/dell-xps13-silver.jpg",
    },
    {
        "name": "Dell Inspiron 15 - Black",
        "category": "laptops",
        "price": "$789",
        "description": "Balanced laptop for office tasks, study, and browsing.",
        "image": "/static/shop/images/products/dell-inspiron15-black.jpg",
    },
    {
        "name": "HP Spectre x360 - Blue",
        "category": "laptops",
        "price": "$1,449",
        "description": "Convertible premium laptop with touchscreen display.",
        "image": "/static/shop/images/products/hp-spectre-x360-blue.jpg",
    },
    {
        "name": "HP Envy 14 - Silver",
        "category": "laptops",
        "price": "$1,099",
        "description": "Creator-focused performance with modern sleek design.",
        "image": "/static/shop/images/products/hp-envy14-silver.jpg",
    },
    {
        "name": "Lenovo ThinkPad X1 - Black",
        "category": "laptops",
        "price": "$1,359",
        "description": "Business-class durability and top keyboard experience.",
        "image": "/static/shop/images/products/lenovo-thinkpad-x1-black.jpg",
    },
    {
        "name": "Asus Zenbook 14 - Gray",
        "category": "laptops",
        "price": "$969",
        "description": "Compact Zenbook model with powerful daily performance.",
        "image": "/static/shop/images/products/asus-zenbook14-gray.jpg",
    },
    {
        "name": "Acer Swift Go - Silver",
        "category": "laptops",
        "price": "$829",
        "description": "Slim and affordable option for students and office use.",
        "image": "/static/shop/images/products/acer-swift-go-silver.jpg",
    },
    {
        "name": "MSI Prestige 14 - White",
        "category": "laptops",
        "price": "$1,179",
        "description": "Modern laptop for professionals with dedicated graphics.",
        "image": "/static/shop/images/products/msi-prestige14-white.jpg",
    },
    {
        "name": "iPhone 15 - Black",
        "category": "phones",
        "price": "$899",
        "description": "Latest iPhone standard model in elegant black.",
        "image": "/static/shop/images/products/iphone-15-black.jpg",
    },
    {
        "name": "iPhone 15 - Blue",
        "category": "phones",
        "price": "$899",
        "description": "Apple iPhone 15 with bright blue finish and dual camera.",
        "image": "/static/shop/images/products/iphone-15-blue.jpg",
    },
    {
        "name": "iPhone 15 Pro - Natural Titanium",
        "category": "phones",
        "price": "$1,199",
        "description": "Pro-level iPhone with titanium body and advanced camera.",
        "image": "/static/shop/images/products/iphone-15-pro-natural.jpg",
    },
    {
        "name": "Samsung Galaxy S24 - Black",
        "category": "phones",
        "price": "$999",
        "description": "Flagship Samsung phone with premium display quality.",
        "image": "/static/shop/images/products/samsung-s24-black.jpg",
    },
    {
        "name": "Samsung Galaxy A55 - Blue",
        "category": "phones",
        "price": "$479",
        "description": "Reliable mid-range Galaxy with long battery life.",
        "image": "/static/shop/images/products/samsung-a55-blue.jpg",
    },
    {
        "name": "Xiaomi 14 - White",
        "category": "phones",
        "price": "$849",
        "description": "Compact premium Android with fast charging support.",
        "image": "/static/shop/images/products/xiaomi-14-white.jpg",
    },
    {
        "name": "Redmi Note 13 - Green",
        "category": "phones",
        "price": "$329",
        "description": "Value-focused Redmi model with smooth display refresh.",
        "image": "/static/shop/images/products/redmi-note-13-green.jpg",
    },
    {
        "name": "Google Pixel 8 - Rose",
        "category": "phones",
        "price": "$799",
        "description": "Clean Android experience with excellent photo quality.",
        "image": "/static/shop/images/products/google-pixel-8-rose.jpg",
    },
    {
        "name": "OnePlus 12 - Green",
        "category": "phones",
        "price": "$879",
        "description": "High-performance OnePlus flagship with fluid interface.",
        "image": "/static/shop/images/products/oneplus-12-green.jpg",
    },
    {
        "name": "Oppo Reno 11 - Gold",
        "category": "phones",
        "price": "$599",
        "description": "Stylish phone with balanced camera and battery features.",
        "image": "/static/shop/images/products/oppo-reno11-gold.jpg",
    },
    {
        "name": "Huawei Nova 12 - Purple",
        "category": "phones",
        "price": "$649",
        "description": "Elegant design with strong portrait camera performance.",
        "image": "/static/shop/images/products/huawei-nova12-purple.jpg",
    },
    {
        "name": "Realme 12 - Black",
        "category": "phones",
        "price": "$369",
        "description": "Affordable all-rounder phone for daily use and study.",
        "image": "/static/shop/images/products/realme-12-black.jpg",
    },
    {
        "name": "Afghani Gand Classic",
        "category": "afghani-clothes",
        "price": "$68",
        "description": "Traditional full set with comfortable fabric for daily wear.",
        "image": "/static/shop/images/products/afghani-clothes-1.jpg",
    },
    {
        "name": "Kandahari Embroidered Set",
        "category": "afghani-clothes",
        "price": "$95",
        "description": "Hand-finished embroidery inspired by Kandahari patterns.",
        "image": "/static/shop/images/products/afghani-clothes-2.jpg",
    },
    {
        "name": "Herati Festive Dress",
        "category": "afghani-clothes",
        "price": "$110",
        "description": "Elegant festive dress made for weddings and ceremonies.",
        "image": "/static/shop/images/products/afghani-clothes-3.jpg",
    },
    {
        "name": "Mazar Soft Cotton Gand",
        "category": "afghani-clothes",
        "price": "$59",
        "description": "Soft cotton gand suitable for warm seasons and travel.",
        "image": "/static/shop/images/products/afghani-clothes-4.jpg",
    },
    {
        "name": "Afghan Youth Daily Set",
        "category": "afghani-clothes",
        "price": "$54",
        "description": "Modern-cut traditional set designed for young customers.",
        "image": "/static/shop/images/products/afghani-clothes-5.jpg",
    },
    {
        "name": "Northern Velvet Gand",
        "category": "afghani-clothes",
        "price": "$132",
        "description": "Premium velvet texture with refined Afghan tailoring.",
        "image": "/static/shop/images/products/afghani-clothes-6.jpg",
    },
    {
        "name": "Classic White Perahan Tunban",
        "category": "afghani-clothes",
        "price": "$61",
        "description": "Clean white set for mosque, gatherings, and formal events.",
        "image": "/static/shop/images/products/afghani-clothes-7.jpg",
    },
    {
        "name": "Afghan Winter Wool Set",
        "category": "afghani-clothes",
        "price": "$89",
        "description": "Warm wool blend outfit suitable for winter weather.",
        "image": "/static/shop/images/products/afghani-clothes-8.jpg",
    },
    {
        "name": "Traditional Green Chapan",
        "category": "afghani-clothes",
        "price": "$140",
        "description": "Traditional chapan with rich color and classic stripe style.",
        "image": "/static/shop/images/products/afghani-clothes-9.jpg",
    },
    {
        "name": "Royal Blue Ceremony Gand",
        "category": "afghani-clothes",
        "price": "$125",
        "description": "Ceremony-focused set with elegant stitching details.",
        "image": "/static/shop/images/products/afghani-clothes-10.jpg",
    },
    {
        "name": "Handmade Copper Pot",
        "category": "home-kitchen",
        "price": "$42",
        "description": "Durable Afghan-style copper pot for family cooking.",
        "image": "/static/shop/images/products/home-kitchen-1.jpg",
    },
    {
        "name": "Traditional Serving Dish Set",
        "category": "home-kitchen",
        "price": "$58",
        "description": "Decorative serving dishes for tea and guest tables.",
        "image": "/static/shop/images/products/home-kitchen-2.jpg",
    },
    {
        "name": "Ceramic Tea Pot",
        "category": "home-kitchen",
        "price": "$35",
        "description": "Classic tea pot with insulated handle and secure lid.",
        "image": "/static/shop/images/products/home-kitchen-3.jpg",
    },
    {
        "name": "Family Rice Pot",
        "category": "home-kitchen",
        "price": "$47",
        "description": "Large pot designed for qabuli and family-size meals.",
        "image": "/static/shop/images/products/home-kitchen-4.jpg",
    },
    {
        "name": "Afghan Soup Bowl Collection",
        "category": "home-kitchen",
        "price": "$39",
        "description": "Set of deep bowls ideal for shorwa and soup service.",
        "image": "/static/shop/images/products/home-kitchen-5.jpg",
    },
    {
        "name": "Heavy Base Fry Pan",
        "category": "home-kitchen",
        "price": "$33",
        "description": "Strong base pan for balanced heat and easy frying.",
        "image": "/static/shop/images/products/home-kitchen-6.jpg",
    },
    {
        "name": "Classic Tea Glass Set",
        "category": "home-kitchen",
        "price": "$26",
        "description": "Traditional tea glasses suitable for daily hosting.",
        "image": "/static/shop/images/products/home-kitchen-7.jpg",
    },
    {
        "name": "Traditional Bread Basket",
        "category": "home-kitchen",
        "price": "$18",
        "description": "Woven basket perfect for naan and table presentation.",
        "image": "/static/shop/images/products/home-kitchen-8.jpg",
    },
    {
        "name": "Kitchen Spice Jar Set",
        "category": "home-kitchen",
        "price": "$29",
        "description": "Compact spice jars for organized Afghan cooking.",
        "image": "/static/shop/images/products/home-kitchen-9.jpg",
    },
    {
        "name": "Copper Serving Tray",
        "category": "home-kitchen",
        "price": "$44",
        "description": "Hand-polished tray for tea service and guest tables.",
        "image": "/static/shop/images/products/home-kitchen-10.jpg",
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


def home(request):
    featured_products = [
        item
        for item in PRODUCTS
        if item["category"] in ("afghani-clothes", "home-kitchen")
    ][:8]
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
