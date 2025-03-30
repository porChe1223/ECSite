from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from order.models import OrderItem
from .forms import OrderForm


@login_required
def make_order(request):
    """""""""""""""""
    注文ビュー
    """""""""""""""""
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cart_cartItem.all() if cart else []
    total_price = sum(item.get_total_price() for item in cart_items) if cart_items else 0

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # カート取得（またはNone）
            cart = Cart.objects.filter(user=request.user).first()
            if not cart or not cart.cart_cartItem.exists():
                # カートが空なら注文させない
                form.add_error(None, "カートが空です。商品を追加してください。")
                return render(request, 'order/make_order.html', {'form': form})

            # Orderを作成
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            # カート内の商品を注文アイテムにコピー
            for cart_item in cart.cart_cartItem.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    product_name=cart_item.product.name,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity
                )

            # カートを空にする
            cart.cart_cartItem.all().delete()

            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'order/make_order.html', {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def order_success(request):
    """""""""""""""""
    注文完了ビュー
    """""""""""""""""
    return render(request, 'order/order_success.html')
