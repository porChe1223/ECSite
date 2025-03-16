# Django
from django.urls import path
from django.conf.urls.static import static
# viewファイル
from . import views
# coreアプリ
from core import settings

app_name = "account"

urlpatterns = [
    path("", views.IndexView.as_view(), name="shop"),
    path('signup/', views.SignupView.as_view(), name="signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
