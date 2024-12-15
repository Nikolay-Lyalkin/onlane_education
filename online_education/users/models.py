from django.contrib.auth.models import AbstractUser
from django.db import models


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
