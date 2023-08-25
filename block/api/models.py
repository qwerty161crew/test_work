from django.db import models


class Content(models.Model):
    text = models.CharField(max_length=200)
    video = models.URLField()
    slug = models.SlugField(unique=True)

    pub_date = models.DateTimeField(auto_now_add=True)


class Views(models.Model):
    views = models.ForeignKey(
        Content, related_name="post_views",
        blank=True, on_delete=models.CASCADE)
