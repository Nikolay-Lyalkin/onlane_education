from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Course, Lesson, Subscribe
from .paginators import PaginationCourse, PaginationLesson
from .permissions import IsModerator, IsOwner
from .serializers import CourseSerializer, LessonSerializer, CourseListSerializer, LessonCreateSerializer, \
    SubscribeSerializer, CourseRetrieveSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationCourse


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonCreateSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationLesson


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscribeAPIView(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, requests, *args, **kwargs):
        user = requests.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Subscribe.objects.filter(course=course_id, user=user.id)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'

        else:
            subscribe = Subscribe(course=course_item, user=user)
            subscribe.save()
            message = 'подписка добавлена'

        return Response({"message": message})
