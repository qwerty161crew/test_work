from django.core.management.base import BaseCommand

from api.models import Content, BlockContents

DATES = (
    ['videos/test_video.MOV', 'slug1'],
    ['videos/test_video.MOV', 'slug2']
)

TITLE = 'title'


class Command(BaseCommand):
    def handle(self, *args, **options):
        for data in DATES:
            Content.objects.create(
                video=data[0],
                slug=data[1]
            )

        content = Content.objects.all()
        block = BlockContents.objects.create(title=TITLE)
        block.content.set(content)
