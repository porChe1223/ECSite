# Django
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
# 自動翻訳
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """""""""""""""""""""""
    ユーザー管理を扱うクラス
    """""""""""""""""""""""
    def _create_user(self, email, password, **extra_fields):
        """""""""""""""""""""""
        ユーザー作成の共通部分
        """""""""""""""""""""""
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    
    def create_user(self, email, password=None, **extra_fields):
        """""""""""""""""
        一般ユーザー作成
        """""""""""""""""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )
    

    def create_superuser(self, email, password, **extra_fields):
        """""""""""""""""""""""""""""""""""""""
        スーパーユーザー（管理者 + 従業員）作成
        """""""""""""""""""""""""""""""""""""""
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )
    

class User(AbstractBaseUser, PermissionsMixin):
    """""""""""""""""""""
    ユーザ情報を扱うクラス
    """""""""""""""""""""
    # メールアドレス
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True,
        null = False
    )
    # 姓
    first_name = models.CharField(
        verbose_name=_("first_name"),
        max_length=150,
        null=False,
        blank=False
    )
    # 名
    last_name = models.CharField(
        verbose_name=_("last_name"),
        max_length=150,
        null=False,
        blank=False
    )
    # 誕生日
    birth_date = models.DateField(
        verbose_name=_("birth_date"),
        blank=True,
        null=False
    )
    # 管理者か否か
    is_superuser = models.BooleanField(
        verbose_name=_("is_superuer"),
        default=False
    )
    # 従業員か否か
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    # 活動中か否か
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    # 作成日時
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    # 更新日時
    updated_at = models.DateTimeField(
        verbose_name=_("updateded_at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email' # ログイン時、ユーザー名の代わりにemailを使用
    # スーパーユーザー作成時に設定する要素
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birth_date']

    # 管理サイトでアカウントID確認
    def __str__(self):
        return self.email
