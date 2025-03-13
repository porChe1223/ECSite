# Django
from django.urls import path
# viewページ
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:pk>', views.product_detail, name="product_detail"),
]