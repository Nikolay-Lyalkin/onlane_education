from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from materials.models import Course, Lesson


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@yandex.ru', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        data = {
            "name": "Test_create"
        }

        response = self.client.post(
            "/course/create/",
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'name': 'Test_create', 'preview': None, 'description': None, 'user': 1}
        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_create_subscribe(self):
        course = Course.objects.create(name="Test_subscribe")
        data = {
            "course": course.id,
            "user": self.user
        }
        response = self.client.post(
            "/subscribe/",
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'подписка добавлена'}
        )

        response = self.client.post(
            "/subscribe/",
            data=data
        )

        self.assertEquals(
            response.json(),
            {'message': 'подписка удалена'}
        )

    def test_create_lesson(self):
        data = {
            "name": "Test_create",
        }

        response = self.client.post(
            "/lesson/create/",
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'name': 'Test_create', 'description': None, 'preview': None, 'link_on_video': None,
             'course': None,
             'user': 2}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        Lesson.objects.create(name="Test_list")

        response = self.client.get(
            "/lesson/",
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 4, 'name': 'Test_list', 'description': None, 'preview': None, 'link_on_video': None,
                 'course': None,
                 'user': None}]}
        )

    def test_delete_lesson(self):
        Lesson.objects.create(name="Test_delete", user=self.user)

        response = self.client.delete(
            "/lesson/2/delete/"
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_put_lesson(self):
        Lesson.objects.create(name="Test_put", user=self.user)
        data = {
            "name": "Test123"
        }

        response = self.client.put(
            "/lesson/5/update/",
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 5, 'name': 'Test123', 'description': None, 'preview': None, 'link_on_video': None, 'course': None,
             'user': 7}
        )

    def test_detail_lesson(self):
        Lesson.objects.create(name="Test_detail", user=self.user)

        response = self.client.get(
            "/lesson/3/",
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 3, 'name': 'Test_detail', 'description': None, 'preview': None, 'link_on_video': None,
             'course': None, 'user': 5}
        )
