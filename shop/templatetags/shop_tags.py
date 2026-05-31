from django import template
import datetime as dt
from ..models import Categories, Products

register = template.Library()


@register.simple_tag()
def cur_date():
    current_date = dt.date.today()
    return "It Works!"


@register.inclusion_tag("product_info.html")
def product_detail(post):
    return post


@register.inclusion_tag("includes/side_bar.html")
def load_category_list():
    cat = Categories.objects.all()
    return {"categories": cat}


@register.inclusion_tag("includes/mobile.html")
def load_category_list_mobile():
    cat = Categories.objects.all()
    return {"categories": cat}


@register.simple_tag()
def categories():
    cat = Categories.objects.all()
    return cat


@register.simple_tag()
def all_products():
    cat = Products.objects.all()
    return cat
