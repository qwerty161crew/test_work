import django_filters.rest_framework
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from .serializers import ContentSeralizers, ListContentSerializers
from .models import Content


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ListContentSerializers
    permission_classes = (AllowAny, )
    pagination_class = PageNumberPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_content(self, request, slug):
        content = Content.objects.get(slug=slug)
        serializer = ContentSeralizers(content).data
        return Response(status=status.HTTP_200_OK, data=serializer)
