from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from .models import Course, Lesson, Payment, Subscribe
from .validators import LinkOnVideoValidator


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"


class CourseRetrieveSerializer(ModelSerializer):
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_subscribe(self, instance):
        request = self.context["request"]
        user = request.user
        subscribe_user = Subscribe.objects.filter(course=instance, user=user)
        if subscribe_user:
            return "вы подписаны на данный курс"
        else:
            return "вы не подписаны на данный курс"


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonCreateSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LinkOnVideoValidator(fields="link_on_video"),
        ]


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class CourseListSerializer(ModelSerializer):
    quantity_lessons = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_quantity_lessons(self, instance):
        if instance.lesson.all():
            return len(instance.lesson.all())
        return 0
