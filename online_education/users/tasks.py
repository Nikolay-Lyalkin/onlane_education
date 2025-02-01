from datetime import datetime

from celery import shared_task

from .models import User


@shared_task
def check_last_login():
    users = User.objects.all()
    for user in users:
        date = user.last_login
        if date:
            login_days_ago = (datetime.utcnow() - date.replace(tzinfo=None)).days
            if login_days_ago > 30:
                user.is_active = False
                user.save()
