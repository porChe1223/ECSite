# Django
from django.db import models


class Cart(models.Model):
    """""""""""""""""""""""
    カート情報を扱うクラス
    """""""""""""""""""""""
    # メタデータ（全体情報）
    class Meta:
      verbose_name = "カート"
      verbose_name_plural = "カート"
    # ユーザー
    user = models.ForeignKey(
      'account.User',
      verbose_name='ユーザー',
      on_delete=models.CASCADE,
      related_name='cart'
    )
    # 商品
    product = models.ForeignKey(
      'shop.Product',
      verbose_name='商品',
      on_delete=models.CASCADE,
      related_name='cart_items'
    )
    # 数量
    quantity = models.PositiveIntegerField(
        verbose_name='数量',
        default=1
    )
    # 追加日時
    created_at = models.DateTimeField(
        verbose_name='追加日時',
        auto_now_add=True
    )
    # 更新日時
    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )

    # 管理サイトでカート確認
    def __str__(self):
        return f"{self.user.email}: {self.product.name} x {self.quantity} -> {self.get_total_price()}円"
    
    # カート内の商品小計（価格 x 数量）
    def get_total_price(self):
        return self.product.price * self.quantity
    