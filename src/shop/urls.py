# Django
from django.urls import path
from django.conf.urls.static import static
# coreアプリ
from core import settings
# viewページ
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)