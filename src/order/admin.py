# Django
from django.contrib import admin
# Cartモデル
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'product_name', 'price', 'quantity')
    can_delete = False

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    display = 'user'
    list_filter = ('payment_way', 'status', 'created_at')
    search_fields = ('user__email', 'postal_code', 'address')
    readonly_fields = ('user', 'postal_code', 'address', 'payment_way', 'created_at', 'updated_at')

admin.site.register(Order, OrderAdmin)