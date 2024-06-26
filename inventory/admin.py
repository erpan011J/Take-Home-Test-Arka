from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Client

class CustomUserAdmin(UserAdmin):
    exclude = ('password', 'name')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Client)
