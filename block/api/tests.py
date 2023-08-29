from django.test import TestCase, Client
from http import HTTPStatus

from .models import Content, BlockContents, Views

CONTENT_LIST = '/api/content/'
CONTENT_DETAIL_TITLE_1 = '/api/content/title_1/'
CONTENT_DETAIL_TITLE_2 = '/api/content/title_2/'
GET_URL = 10


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = Client()

        cls.content = Content.objects.create(
            slug='slug', video='videos/vine.MOV')

        cls.content_2 = Content.objects.create(
            slug='slug_2', video='videos/min.MOV')

        cls.block_content = BlockContents.objects.create(title='title_1')
        cls.block_content.content.set(Content.objects.filter(slug='slug'))

        cls.block_content_2 = BlockContents.objects.create(title='title_2')
        cls.block_content_2.content.set(Content.objects.filter(slug='slug_2'))

    def test_status_code_response(self):
        cases = [
            [CONTENT_LIST, self.user, HTTPStatus.OK],
            [CONTENT_DETAIL_TITLE_1, self.user, HTTPStatus.OK],
            [CONTENT_DETAIL_TITLE_2, self.user, HTTPStatus.OK],
        ]
        for url, client, answer in cases:
            with self.subTest(url=url, client=client, answer=answer):
                self.assertEqual(client.get(url).status_code, answer)

    def test_views_content(self):
        for i in range(1, (GET_URL + 1)):
            self.client.get(CONTENT_DETAIL_TITLE_1)
            views = Views.objects.filter(views=self.content).count()
            self.assertEqual(i, views)

    def test_block_content(self):
        response = self.client.get(CONTENT_DETAIL_TITLE_1)
        response_2 = self.client.get(CONTENT_DETAIL_TITLE_2)
        self.assertNotEqual(response.data, response_2.data)
