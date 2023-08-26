from rest_framework import serializers

from .models import Content, Views


class ContentSeralizers(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('__all__')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data, instance)
        Views.objects.create(views=instance)
        total_views = Views.objects.filter(views=data['id']).count()
        data['total_views'] = total_views
        return data


class ListContentSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:content-detail', read_only=True, lookup_field='slug')

    class Meta:
        model = Content
        fields = ('id', 'text', 'url')
