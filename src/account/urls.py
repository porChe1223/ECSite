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
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
