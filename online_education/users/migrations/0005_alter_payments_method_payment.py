# Generated by Django 5.1.4 on 2024-12-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_payments_date_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="method_payment",
            field=models.CharField(
                choices=[
                    ("cash", "Наличные"),
                    ("transfer_to_account", "Перевод на счёт"),
                ],
                verbose_name="Способ оплаты",
                max_length=50,
            ),
        ),
    ]
