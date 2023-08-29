from django.test import TestCase, Client
from http import HTTPStatus

from .models import Content, Views

CONTENT_LIST = '/api/content/'
CONTENT_DETAIL = '/api/content/slug/'


class ContentTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.content = Content.objects.create(
            title='Тестовый пост',
            slug='slug',
            video='videos/test_video.MOV'
        )
        cls.guest_client = Client()
        cls.get_url = 10

    def test_status_code(self):
        cases = [
            [CONTENT_LIST, self.guest_client, HTTPStatus.OK],
            [CONTENT_DETAIL, self.guest_client, HTTPStatus.OK]
        ]
        for url, client, answer in cases:
            with self.subTest(url=url, client=client, answer=answer):
                self.assertEqual(client.get(url).status_code, answer)

    def test_count_views(self):
        for i in range(1, (self.get_url + 1)):
            self.guest_client.get(CONTENT_DETAIL)
            count_views = Views.objects.filter(views=self.content).count()
            self.assertEqual(i, count_views)
