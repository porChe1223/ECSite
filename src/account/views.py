# Django
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm


class IndexView(TemplateView):
    """""""""""""""
    ホームビュー
    """""""""""""""
    template_name = "shop.html"


class SignupView(CreateView):
    """""""""""""""""
    ユーザ登録ビュー
    """""""""""""""""
    form_class = SignUpForm                      # 作成した登録用フォームを設定
    template_name = "account/signup.html"
    success_url = reverse_lazy("account:shop")   # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(
                 email = email,
                 password = password
               )
        login(self.request, user)

        # セッション保存用のnextパラメータがあるか確認
        next_url = self.request.POST.get("next")
        if next_url:
            return redirect(next_url)
        
        return response
    

class LoginView(BaseLoginView):
    """""""""""""""
    ログインビュー
    """""""""""""""
    form_class = LoginForm
    template_name = "account/login.html"


class LogoutView(BaseLogoutView):
    """""""""""""""""
    ログアウトビュー
    """""""""""""""""
    success_url = reverse_lazy("account:shop")
