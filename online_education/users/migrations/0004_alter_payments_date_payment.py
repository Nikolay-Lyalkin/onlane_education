# Generated by Django 5.1.4 on 2024-12-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="date_payment",
            field=models.DateField(auto_now_add=True, verbose_name="Дата оплаты"),
        ),
    ]