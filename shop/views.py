from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Categories,  Feedbacks, Invoices, Products
from django.core.paginator import Paginator
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

def update_categories(request):
    try:
        # --- RENAME CATEGORIES ---
        # Update category 3 from Afghani Clothes to TVs
        try:
            cat3 = Categories.objects.get(ct_id=3)
            cat3.name = "TVs"
            cat3.description = "Premium 4K Smart TVs"
            cat3.save()
        except:
            Categories.objects.create(
                ct_id=3, name="TVs", description="Premium 4K Smart TVs")

        # Update category 4 from Home & Kitchen to Headphones
        try:
            cat4 = Categories.objects.get(ct_id=4)
            cat4.name = "Headphones"
            cat4.description = "Premium Noise-Canceling Headphones"
            cat4.save()
        except:
            Categories.objects.create(
                ct_id=4, name="Headphones", description="Premium Noise-Canceling Headphones")

        # Ensure categories 1 and 2 are correct
        for ct_id, name, desc in [
            (1, "Laptops", "Premium Laptops for Work & Gaming"),
            (2, "Phones", "Premium Smartphones"),
        ]:
            try:
                cat = Categories.objects.get(ct_id=ct_id)
                cat.name = name
                cat.description = desc
                cat.save()
            except:
                Categories.objects.create(
                    ct_id=ct_id, name=name, description=desc)

        # --- UPDATE PRODUCT IMAGES ---
        # Get category IDs
        try:
            cat_tvs = Categories.objects.get(ct_id=3)
            cat_headphones = Categories.objects.get(ct_id=4)
        except:
            pass

        # List of TV photos
        tv_photos = [
            "best-LG-5tv.png", "design-mediumsamsungtv.jpg", "flagshiptv.jpg",
            "hisenserukutv.jpg", "lg3tv.jpg", "lgtv.jpg", "panasonctv.jpg",
            "philipstv.jpg", "samsungmoderntv.jpg", "samsungtv.jpg",
            "sonytv.jpg", "tcltv.jpg", "toshibatv.jpg", "tv1.jpg",
            "tv2.jpg", "tv3.jpg", "tv4.jpg", "tv5.jpg", "xiaomitv.webp"
        ]

        # List of Headphone photos
        headphone_photos = [
            "Black-Airpod-Pro.jpg", "C9044headphones.jpg", "acideyeheadphone.jpeg",
            "airpod1.jpg", "airpodpro.jpg", "appleairpod.webp",
            "appleshapedairpod.jpg", "black_cabled_headphone.jpg",
            "blue_cabled_headphone.jpg", "earbudsheadphone.jpg",
            "gamingheadphones.jpg", "girlheadphone.jpg",
            "greengamingheadphones.jpg", "headphone1.jpg", "headphone2.jpg",
            "noisecancelligheadphone.webp", "oyellexheadphone.jpg",
            "xboxheadphones.jpg"
        ]

        # Update products in category 3 (TVs)
        try:
            tvs_products = Products.objects.filter(category=3)
            for i, product in enumerate(tvs_products):
                if i < len(tv_photos):
                    product.image = tv_photos[i]
                    product.hot = True
                    product.save()
        except:
            pass

        # Update products in category 4 (Headphones)
        try:
            headphones_products = Products.objects.filter(category=4)
            for i, product in enumerate(headphones_products):
                if i < len(headphone_photos):
                    product.image = headphone_photos[i]
                    product.hot = True
                    product.save()
        except:
            pass

        return redirect(reverse("shop:home"))
    except:
        return redirect(reverse("shop:home"))


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
