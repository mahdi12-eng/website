from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address


class CutomUserAdmin(UserAdmin):
    model = User
    list_display = ["name", "last_name", "email", "is_staff"]
    list_filter = ["name", "email", "is_staff"]
    search_fields = ["name", "email"]
    ordering = ["name"]
    fieldsets = (
        ("Authentications", {
            "fields": (
                "name", "last_name", "email", "address", "birth_date"
            ),
        }),
    )


admin.site.register(Address)
admin.site.register(User, CutomUserAdmin)
