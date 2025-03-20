# Django
from django.db import models


class Product(models.Model):
    """""""""""""""""""""""""""
    商品に関する情報を扱うクラス
    """""""""""""""""""""""""""
    # メタデータ（全体情報）
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
    # 画像
    image = models.ImageField(
        verbose_name = '画像',
        upload_to = 'image/'
    )
    # 名前
    name = models.CharField(
        verbose_name = '名前',
        max_length=50,
        unique=True,
        null = False,
        blank=False
    )
    # 価格
    price = models.IntegerField(
        verbose_name = '価格'
    )
    description = models.TextField(
        verbose_name = '説明'
    )

    # 管理サイトで商品名確認
    def __str__(self):
        return self.name
