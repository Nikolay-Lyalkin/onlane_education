from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import UsersConfig
from . import views

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")

urlpatterns = [] + router.urls
