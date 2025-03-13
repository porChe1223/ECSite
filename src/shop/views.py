from django.shortcuts import render
from .models import Product


def shop(request):
    products = Product.objects.all()

    return render(request, 'shop.html', {'products': products})
