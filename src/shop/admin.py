# Django
from django.contrib import admin
# Productモデル
from .models import Product


admin.site.register(Product) # Productモデルを登録