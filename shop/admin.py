from django.contrib import admin
from .models import *


admin.site.register(Categories)

admin.site.register(Feedbacks)
admin.site.register(Invoices)
admin.site.register(Orders)
admin.site.register(OrderDetail)
admin.site.register(PaymentMethod)
admin.site.register(Payments)
admin.site.register(Products)
admin.site.register(Status)
