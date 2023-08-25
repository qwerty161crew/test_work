from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from .serializers import ContentSeralizers, ListContentSerializers
from .models import Content


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSeralizers
    permission_classes = (AllowAny, )
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('list'):
            return ListContentSerializers
        return ContentSeralizers
