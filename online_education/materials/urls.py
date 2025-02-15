from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"subscribe", views.SubscribeAPIView, basename="subscribe")

urlpatterns = [
    # Course
    path("course/", views.CourseListAPIView.as_view(), name="course_list"),
    path("course/create/", views.CourseCreateAPIView.as_view(), name="course_create"),
    path("course/<int:pk>/", views.CourseRetrieveAPIView.as_view(), name="course_retrieve"),
    path("course/<int:pk>/delete/", views.CourseDeleteAPIView.as_view(), name="course_delete"),
    path("course/<int:pk>/update/", views.CourseUpdateAPIView.as_view(), name="course_update"),
    # Lesson
    path("lesson/create/", views.LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/", views.LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", views.LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/<int:pk>/delete/", views.LessonDeleteAPIView.as_view(), name="lesson_delete"),
    path("lesson/<int:pk>/update/", views.LessonUpdateAPIView.as_view(), name="lesson_update"),
    # Payment
    path("payment/create/", views.PaymentCreateAPIView.as_view(), name="payment_create"),
] + router.urls
