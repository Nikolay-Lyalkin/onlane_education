# Generated by Django 5.1.4 on 2024-12-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_payments_method_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="method_payment",
            field=models.CharField(
                choices=[
                    ("наличные", "Наличные"),
                    ("перевод на счёт", "Перевод на счёт"),
                ],
                verbose_name="Способ оплаты",
                max_length=50,
            ),
        ),
    ]
