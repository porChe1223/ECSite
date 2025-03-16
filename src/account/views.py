# Django
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


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
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(
                 account_id = account_id,
                 password = password
               )
        login(self.request, user)
        return response
