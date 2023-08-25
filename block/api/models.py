from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    video = models.URLField()

    pub_date = models.DateTimeField(auto_now_add=True)


class Views(models.Model):
    views = models.ForeignKey(
        Content, related_name="post_views",
        blank=True, on_delete=models.CASCADE)
