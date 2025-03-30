# Django
from django import forms
# Userモデル
from .models import Order


class OrderForm(forms.ModelForm):
    """""""""""""""""
    注文フォーム
    """""""""""""""""
    class Meta:
        model = Order
        fields = (
            "postal_code",
            "address",
            "payment_way",
        )
        widgets = {
            'payment_way': forms.Select(choices=Order.PaymentWay.choices),
        }

    # フロント整形
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["postal_code"].help_text=(
            "必須入力です。\n"
            "半角数字で入力してください。\n"
            "ハイフン（-）は不要です。\n"
        )
        self.fields["address"].help_text="必須入力です。"
        self.fields["payment_way"].help_text="必須入力です。"
