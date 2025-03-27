# Django
from django.urls import path
from django.conf.urls.static import static
# coreアプリ
from core import settings
# viewページ
from . import views


urlpatterns = [
    path('', views.show_shop, name='show_shop'),                    # 商品一覧
    path('<int:pk>/', views.product_detail, name='product_detail'), # 商品詳細
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)