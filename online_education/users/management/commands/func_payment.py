from django.core.management.base import BaseCommand
from materials.models import Course
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.filter(id=1)[0]
        course = Course.objects.filter(id=4)[0]
        payment_model = Payments(user=user, paid_course=course, sum_payment=180000, method_payment=Payments.CASH)
        payment_model.save()
