from rest_framework import viewsets, generics

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer, CourseListSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
