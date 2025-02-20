from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # User
    path("user/create/", views.UserCreateAPIView.as_view(), name="user_create"),
    path("user/", views.UserListAPIView.as_view(), name="user_list"),
    path("user/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user/<int:pk>/delete/", views.UserDeleteAPIView.as_view(), name="user_delete"),
    path("user/<int:pk>/update/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("user/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Payments
    path("payments/create/", views.PaymentsCreateAPIView.as_view(), name="payment_create"),
    path("payments/", views.PaymentsListAPIView.as_view(), name="payment_list"),
    path(
        "payment/<int:pk>/",
        views.PaymentsRetrieveAPIView.as_view(),
        name="payment_retrieve",
    ),
    path(
        "payment/<int:pk>/delete/",
        views.PaymentsDeleteAPIView.as_view(),
        name="payment_delete",
    ),
    path(
        "payment/<int:pk>/update/",
        views.PaymentsUpdateAPIView.as_view(),
        name="payment_update",
    ),
]
