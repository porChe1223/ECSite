# Django
from django.contrib.auth.forms import UserCreationForm
# Userモデル
from .models import User


class SignUpForm(UserCreationForm):
    """""""""""""""""""""
    ユーザ作成フォーム
    """""""""""""""""""""
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
            "birth_date",
        )
