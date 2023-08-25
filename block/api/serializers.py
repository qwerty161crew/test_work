from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Content, Views


class ContentSeralizers(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('__all__')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        Views.objects.create(views=instance)
        total_views = Views.objects.filter(views=data['id']).count()
        data['total_views'] = total_views
        return data


class ListContentSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='content-detail', read_only=True)

    class Meta:
        model = Content
        fields = ('id', 'text', 'url')
        # extra_kwargs = {
        #     'url': {'view_name': 'api:content'}
        # }
