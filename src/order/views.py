from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm


@login_required
def make_order(request):
    """""""""""""""""
    注文ビュー
    """""""""""""""""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order/make_order.html', {'form': form})


@login_required
def order_success(request):
    """""""""""""""""
    注文完了ビュー
    """""""""""""""""
    return render(request, 'order/order_success.html')
