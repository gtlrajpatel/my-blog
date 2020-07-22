from django.db import models
from django.conf import settings


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogAPI(TimeStampedModel):
    title = models.CharField(max_length=40, default=None)
    text = models.TextField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs',  on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)


class Comment(TimeStampedModel):
    text = models.TextField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogAPI, related_name='comments',  on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
