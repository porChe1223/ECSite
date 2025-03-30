# Django
from django.contrib import admin
# Cartモデル
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0  # 余分な空のフォームを表示しない

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('user', 'created_at', 'get_total_price')

admin.site.register(Cart, CartAdmin)