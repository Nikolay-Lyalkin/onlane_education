from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name="Название курса")
    preview = models.ImageField(upload_to="course image/", blank=True, null=True)
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        db_table = "courses"


class Lesson(models.Model):
    name = models.CharField(verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", blank=True, null=True)
    preview = models.ImageField(upload_to="lesson image/", blank=True, null=True)
    link_on_video = models.URLField(verbose_name="сылка на видео урока", blank=True, null=True)
    course = models.ForeignKey(
        Course, blank=True, null=True, on_delete=models.SET_NULL, related_name="lesson", verbose_name="Курс"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        db_table = "lessons"