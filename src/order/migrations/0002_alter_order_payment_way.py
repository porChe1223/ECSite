# Generated by Django 3.2.12 on 2025-03-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_way',
            field=models.IntegerField(choices=[('代金引換', '代金引換'), ('銀行振込', '銀行振込'), ('クレジットカード', 'クレジットカード')], default='代金引換', verbose_name='支払方法'),
        ),
    ]
