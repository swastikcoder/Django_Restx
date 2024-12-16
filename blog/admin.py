from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser


class CustomUserAdmin(UserAdmin):
    list_display = ("username","email","first_name", "last_name")


admin.site.register(CustomerUser,CustomUserAdmin)
