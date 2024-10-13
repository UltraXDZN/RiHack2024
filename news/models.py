from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from HackatonTemplate.ai.gepetto import getTopic


class NewsFull(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField()
    banner = models.ImageField(upload_to='news/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if topic is empty before calling getTopic
        if not self.topic:
            self.topic = getTopic(self.content)
        super(NewsFull, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
