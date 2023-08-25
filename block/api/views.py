from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from .serializers import ContentSeralizers


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSeralizers
    permission_classes = (AllowAny, )
    pagination_class = PageNumberPagination
