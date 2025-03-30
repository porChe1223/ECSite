# Django
from django.contrib import admin
# Cartモデル
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'created_at')
    can_delete = False

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    display = 'user'
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__email',)

admin.site.register(Cart, CartAdmin)