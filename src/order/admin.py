# Django
from django.contrib import admin
# Cartモデル
from .models import Order

admin.site.register(Order) # Cartモデルを登録