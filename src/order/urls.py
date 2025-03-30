# Django
from django.urls import path
# viewページ
from . import views


urlpatterns = [
    path('order/', views.make_order, name='make_order'),                # 注文確認
    path('order/success/', views.order_success, name='order_success'),  # 注文完了
]