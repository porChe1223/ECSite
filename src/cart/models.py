# Django
from django.db import models


class Cart(models.Model):
    """""""""""""""""""""""
    カート情報を扱うクラス
    """""""""""""""""""""""
    class Meta:
        """""""""""""""""""""""""""""
        メタデータ（データの名称）
        """""""""""""""""""""""""""""
        verbose_name = "カート"
        verbose_name_plural = "カート"
      
    # ユーザー
    user = models.OneToOneField(
        'account.User',
        verbose_name='ユーザー',
        on_delete=models.CASCADE,
        related_name='cart_user'
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
        return f"[ID: {self.user_id}] {self.user.email}のカート"


class CartItem(models.Model):
    """""""""""""""""""""""""""""""""""
    カート内の商品情報を扱うクラス
    """""""""""""""""""""""""""""""""""
    class Meta:
        """""""""""""""""""""""""""""
        メタデータ（データの名称）
        """""""""""""""""""""""""""""
        verbose_name = "カートアイテム"
        verbose_name_plural = "カートアイテム"
      
    # カート
    cart = models.ForeignKey(
      Cart,
      verbose_name='カート',
      on_delete=models.CASCADE,
      related_name='cart_cartItem'
    )
    # 商品
    product = models.ForeignKey(
      'shop.Product',
      verbose_name='商品',
      on_delete=models.CASCADE,
      related_name='cart_cartItem'
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

    # 管理サイトでカート内の商品確認
    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity} -> {self.get_total_price()}円"
    