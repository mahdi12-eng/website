from django import template
import datetime as dt
register = template.Library()

@register.simple_tag()
def cur_date():
    current_date=dt.date.today()
    return 'It Works!'