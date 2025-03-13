# Django
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
# coreアプリ
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), # shopアプリ
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
