from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey('auth.User')

    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    publish_date = models.DateTimeField(null = True, blank = True )
