# Django
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
# coreアプリ
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),    # 管理者アプリ
    path('', include('shop.urls')),     # shopアプリ
    path('', include('account.urls')),  # accountアプリ
    path('', include('cart.urls')),     # cartアプリ
    path('', include('order.urls')),    # orderアプリ
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
