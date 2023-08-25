from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from .models import Content, Views


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class ContentSeralizers(serializers.ModelSerializer):
    author = AuthorSerializers()

    class Meta:
        model = Content
        fields = ('__all__')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        Views.objects.create(views=data['id'])
        total_views = Views.objects.filter(views=data['id']).count()
        data['total_views'] = total_views
        return data
