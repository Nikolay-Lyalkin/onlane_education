from config import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name="Название курса", max_length=50)
    preview = models.ImageField(upload_to="course image/", blank=True, null=True)
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True, max_length=1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_course",
        verbose_name="пользователь",
    )
    amount = models.PositiveIntegerField(verbose_name="цена", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        db_table = "courses"


class Lesson(models.Model):
    name = models.CharField(verbose_name="Название урока", max_length=1000)
    description = models.TextField(verbose_name="Описание урока", blank=True, null=True, max_length=1000)
    preview = models.ImageField(upload_to="lesson image/", blank=True, null=True)
    link_on_video = models.URLField(verbose_name="сылка на видео урока", blank=True, null=True)
    course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="lesson",
        verbose_name="Курс",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="lesson",
        verbose_name="пользователь",
    )
    amount = models.PositiveIntegerField(verbose_name="цена", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        db_table = "lessons"


class Subscribe(models.Model):
    course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="subscribe_on_course",
        verbose_name="Подписка на курс",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="user_subscribe",
        verbose_name="пользователь",
    )

    def __str__(self):
        return f"{self.user}-{self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        db_table = "subscribe"


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_payment",
        verbose_name="пользователь",
    )
    course_payment = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="payment_for_course",
        verbose_name="Платёж за курс",
    )
    link_on_payment = models.URLField(max_length=400, verbose_name="ссылка на оплату", blank=True, null=True)

    def __str__(self):
        return f"{self.user}-{self.course_payment}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
        db_table = "paid_courses"
