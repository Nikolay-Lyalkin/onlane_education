from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from .models import User, Payments
from .serializers import UserSerializer, PaymentsSerializer, PaymentsListSerializer, UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "paid_course",
        "paid_lesson",
        "method_payment",
    )
    ordering_fields = ("date_payment",)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDeleteAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
