from celery import shared_task
from django.core.mail import send_mail
from users.models import User

from .models import Course, Subscribe


@shared_task
def email_about_update(course_id):
    course = Course.objects.filter(id=course_id).first()
    subscribe_list = Subscribe.objects.filter(course_id=course_id)
    for subscribe in subscribe_list:
        user = User.objects.filter(id=subscribe.user_id).first()
        sent_mail = send_mail(
            "Обновление курса по вашей подписке в SkyPro",
            f"Вышло новое обновление для курса {course}",
            "serega94nn@yandex.ru",
            [user.email],
        )
