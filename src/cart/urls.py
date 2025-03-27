# Django
from django.urls import path
# viewページ
from . import views


urlpatterns = [
    path('cart/', views.show_cart, name='show_cart'),                          # カートの閲覧
    path('add/<str:pk>/', views.add_to_cart, name='add_to_cart'),              # カートへの追加
    path('add_after_logined/', views.add_to_cart_after_logined, name='add_to_cart_after_logined'), # ログイン後のカート追加
    path('delete/<str:pk>/', views.delete_from_cart, name='delete_from_cart'), # カートから削除
    path('update/<str:pk>/', views.update_cart, name='update_cart'),           # カートの更新
]