from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from .serializers import ContentSeralizers, ListContentSerializers
from .models import Content, BlockContents


class ContentViewSet(viewsets.ModelViewSet):
    queryset = BlockContents.objects.all()
    serializer_class = ListContentSerializers
    permission_classes = (AllowAny, )
    pagination_class = PageNumberPagination

    def get_content(self, request, title):
        block_content = BlockContents.objects.filter(title=title)
        content = Content.objects.filter(
            content_in_block__in=block_content)
        serializer = ContentSeralizers(content, many=True).data
        return Response(status=status.HTTP_200_OK, data=serializer)
