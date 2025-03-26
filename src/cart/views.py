from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart


@login_required
def cart(request):
  """""""""""""""""""""""""""""""""""""""""""""
  ユーザに関するCartクラスの全データをHTMLに送信
  """""""""""""""""""""""""""""""""""""""""""""
  cart_items = Cart.objects.filter(user=request.user)
  total_price = sum(item.get_total_price() for item in cart_items)
  
  return render(request, 'cart/cart.html', {
     'cart_items': cart_items,
     'total_price': total_price
  })


@login_required
@require_POST
def add_to_cart(request, pk):
  """""""""""""""""""""""""""""""""""
  Cartクラスへの商品追加をHTMLに送信
  """""""""""""""""""""""""""""""""""
  product = get_object_or_404(Product, pk=pk)
  quantity = int(request.POST.get('quantity', 1))

  cart_item, created = Cart.objects.get_or_create(
      user=request.user,
      product=product,
      defaults={'quantity': quantity}
  )
  if not created:
      cart_item.quantity += quantity
      cart_item.save()
  
  return redirect('cart')


@login_required
@require_POST
def delete_from_cart(request, pk):
    """""""""""""""""""""""""""""""""""
    Cartクラスへの商品削除をHTMLに送信
    """""""""""""""""""""""""""""""""""
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    cart_item.delete()

    return redirect('cart')


@login_required
@require_POST
def update_cart(request, pk):
    """""""""""""""""""""""""""""
    Cartクラスの更新をHTMLに送信
    """""""""""""""""""""""""""""
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')
