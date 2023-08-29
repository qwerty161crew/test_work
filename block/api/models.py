from django.db import models


class Content(models.Model):
    video = models.FileField(upload_to='videos/', null=True)
    slug = models.SlugField(unique=True)

    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __srt__(self):
        return self.slug[:15]


class Views(models.Model):
    views = models.ForeignKey(
        Content, related_name="post_views",
        blank=True, on_delete=models.CASCADE)


class BlockContents(models.Model):
    content = models.ManyToManyField(
        Content, related_name='content_in_block')
    title = models.CharField(max_length=200, unique=True)
