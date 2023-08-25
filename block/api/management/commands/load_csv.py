import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import Content
DATA = ['ПРОСТО ТЕКСТ', 'https://www.youtube.com/watch?v=Ur24Ms-MD5k', 'slug1']

class Command(BaseCommand):
    def handle(self, *args, **options):
        Content.objects.create(text=DATA[0], video=DATA[1], slug=DATA[2])
