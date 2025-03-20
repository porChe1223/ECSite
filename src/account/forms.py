# 標準ライブラリ
import re # 正規表現
# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.timezone import now
# Userモデル
from .models import User


class SignUpForm(UserCreationForm):
    """""""""""""""""""""
    ユーザ作成フォーム
    """""""""""""""""""""
    birth_date = forms.DateField( # 誕生日はカレンダーウィジェットで選択
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "birth_date",
        )

    # フロント整形
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["email"].help_text="必須入力です。"
        self.fields["first_name"].help_text="必須入力です。"
        self.fields["last_name"].help_text="必須入力です。"
        self.fields["birth_date"].help_text="必須入力です。"
        self.fields["password1"].help_text=(
            "必須入力です。\n"
            "8文字以上20文字以下にしてください。\n"
            "アルファベット・数字・特殊文字を最低1つずつ含んでください。"
        )

    def clean_birth_date(self):
        """""""""""""""""""""""
        誕生日のバリデーション
        -> 未来の日付けはダメ
        """""""""""""""""""""""
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date and birth_date > now().date():
            raise ValidationError("誕生日には未来の日付を設定できません。")
        
        return birth_date
    
    def clean_password1(self):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        パスワードのバリデーション
        -> 8文字以下はダメ
        -> 20文字以上はダメ
        -> 正規表現でアルファベット、数字、特殊文字を含むかチェック
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        password1 = self.cleaned_data.get("password1")
        errors = []
        if password1 and not (8 <= len(password1) <= 20):
            errors.append("パスワードは8文字以上20文字以下にしてください。")
        
        if password1 and not re.search(r"[A-Za-z]", password1):
            errors.append("アルファベットを最低1文字含めてください。")
        
        if password1 and not re.search(r"\d", password1):
            errors.append("数字を最低1文字含めてください。")
        
        if password1 and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password1):
            errors.append("特殊文字（!@#$%^&* など）を最低1文字含めてください。")
        
        if errors:
            raise ValidationError(errors)
        
        return password1


class LoginForm(AuthenticationForm):
    """""""""""""""""
    ログインフォーム
    """""""""""""""""
    class Meta:
        model = User
    
    # フロント整形
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
