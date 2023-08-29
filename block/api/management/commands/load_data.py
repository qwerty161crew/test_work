from django.core.management.base import BaseCommand

from api.models import Content

DATES = (
    ['ПРОСТО ТЕКСТ', 'videos/test_video.MOV', 'slug1'],
    ['Название 2', 'videos/test_video.MOV', 'slug2']
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for data in DATES:
            Content.objects.create(title=data[0],
                                   video=data[1],
                                   slug=data[2])
