from django.contrib import admin
from .models import (
    Address,
    Categories,
    Customers,
    Feedbacks,
    Invoices,
    Orders,
    OrderDetail,
    PaymentMethod,
    Payments,
    Products,
    Status,
)

admin.site.register(Address)
admin.site.register(Categories)
admin.site.register(Customers)
admin.site.register(Feedbacks)
admin.site.register(Invoices)
admin.site.register(Orders)
admin.site.register(OrderDetail)
admin.site.register(PaymentMethod)
admin.site.register(Payments)
admin.site.register(Products)
admin.site.register(Status)
