from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response


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

    def get_content(self, request, slug):
        content = Content.objects.get(slug=slug)
        serializer = ContentSeralizers(content).data
        return Response(status=status.HTTP_200_OK, data=serializer)
