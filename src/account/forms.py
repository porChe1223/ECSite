# Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Userモデル
from .models import User


class SignUpForm(UserCreationForm):
    """""""""""""""""""""
    ユーザ作成フォーム
    """""""""""""""""""""
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "birth_date",
        )


class LoginForm(AuthenticationForm):
    """""""""""""""""
    ログインフォーム
    """""""""""""""""
    class Meta:
        model = User
    
