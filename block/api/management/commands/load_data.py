from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from api.models import Content

DATA = ['ПРОСТО ТЕКСТ', 'https://www.youtube.com/watch?v=Ur24Ms-MD5k', 'slug1']


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Content.objects.filter(slug=DATA[2]).exists():
            Content.objects.create(text=DATA[0], video=DATA[1], slug=DATA[2])
        raise ValidationError('Вы уже создали запись')
