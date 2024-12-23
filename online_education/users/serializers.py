from rest_framework.serializers import ModelSerializer
from .models import User, Payments


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number")


class PaymentsSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class PaymentsListSerializer(ModelSerializer):
    class Meta:
        model = Payments
        if Payments.paid_course:
            fields = ("id", "user", "date_payment", "paid_course", "sum_payment", "method_payment")
        else:
            fields = ("id", "user", "date_payment", "paid_lesson", "sum_payment", "method_payment")


class UserListSerializer(ModelSerializer):
    list_payments = PaymentsListSerializer(source="user", many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
