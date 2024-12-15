from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import MaterialsConfig
from . import views

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"course", views.CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create/", views.LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/", views.LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", views.LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/delete/", views.LessonDeleteAPIView.as_view(), name="lesson_delete"),
    path("lesson/<int:pk>/update/", views.LessonUpdateAPIView.as_view(), name="lesson_update"),
] + router.urls
