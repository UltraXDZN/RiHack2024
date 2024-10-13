from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class NewsFull(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField()
    banner = models.ImageField(upload_to='news/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
