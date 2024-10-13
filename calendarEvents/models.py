from datetime import datetime

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
        # Check if end_time is earlier than start_time
        if self.end_time:
            return self.end_time > self.start_time
        else:
            return False  # Handle the case where end_time is None

    @property
    def duration(self):
        try:
            # If they are strings, convert them to datetime objects
            if isinstance(self.start_time, str):
                start_time_dt = datetime.strptime(self.start_time, "%Y-%m-%dT%H:%M:%S")
            else:
                start_time_dt = self.start_time  # Already a datetime object

            if isinstance(self.end_time, str):
                end_time_dt = datetime.strptime(self.end_time, "%Y-%m-%dT%H:%M:%S")
            else:
                end_time_dt = self.end_time  # Already a datetime object

            # Calculate the duration
            duration = end_time_dt - start_time_dt
            return str(duration)

        except ValueError as e:
            print(f"Error in date conversion: {e}")
            return "Unknown"
