from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_time']

    @property
    def is_past(self):
        if self.end_time:
            return self.end_time < timezone.now()
        else:
            return False  # Or adjust based on your logic

    @property
    def duration(self):
        if self.end_time:
            duration = self.end_time - self.start_time
            return str(duration)
        else:
            return "Unknown"
