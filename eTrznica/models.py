# myapp/models.py
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
