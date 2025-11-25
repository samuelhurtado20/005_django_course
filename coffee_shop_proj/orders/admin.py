from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInlineAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model: Order
    inlines = [OrderItemInlineAdmin]


admin.site.register(Order, OrderAdmin)
