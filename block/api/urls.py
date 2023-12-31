from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContentViewSet


app_name = 'api'


router = DefaultRouter()


urlpatterns = [
    path('', include((router.urls, 'api'))),
    path('content/',
         ContentViewSet.as_view({'get': 'list'}), name='content-list'),
    path('content/<str:title>/',
         ContentViewSet.as_view({'get': 'get_content'}), name='content-detail')
]
