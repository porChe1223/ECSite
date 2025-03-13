# Django
from django.urls import path
# viewページ
from . import views


urlpatterns = [
    path("", views.index, name="shop"),
]