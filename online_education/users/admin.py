from django.contrib import admin

from .models import Payments, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username")


@admin.register(Payments)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_payment",
        "paid_course",
        "paid_lesson",
        "sum_payment",
        "method_payment",
    )
