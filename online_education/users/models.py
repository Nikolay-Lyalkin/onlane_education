from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from materials.models import Course, Lesson


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20, verbose_name="Имя пользователя")
    email = models.EmailField(unique=True, max_length=50, verbose_name="Эоектронная почта")
    phone_number = models.CharField(verbose_name="Эоектронная почта", blank=True, null=True)
    city = models.CharField(verbose_name="Город", blank=True, null=True)
    avatar = models.FileField(upload_to="avatars/", verbose_name="Ваша фотография", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CASH = "наличные"
    TRANSFER_TO_ACCOUNT = "перевод на счёт"
    CAN_PAYMENT = [
        (CASH, "Наличные"),
        (TRANSFER_TO_ACCOUNT, "Перевод на счёт"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", verbose_name="Пользователь")
    date_payment = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="paid_course", verbose_name="курс", blank=True, null=True
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="paid_lesson", verbose_name="урок", blank=True, null=True
    )
    sum_payment = models.PositiveIntegerField(verbose_name="Сумма платежа")
    method_payment = models.CharField(choices=CAN_PAYMENT, verbose_name="Способ оплаты")

    def __str__(self):
        if self.paid_course:
            return f"Оплатил-{self.user}, курс-{self.paid_course}"
        return f"Оплатил-{self.user}, урок-{self.paid_lesson}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        db_table = "payments"
