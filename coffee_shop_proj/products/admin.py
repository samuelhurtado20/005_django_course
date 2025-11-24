from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'description', 'available']
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)
