from django.contrib.auth.models import User
from django.db import models

from HackatonTemplate import settings


class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, related_name='cities', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'county')

    def __str__(self):
        return f"{self.name}, {self.county.name}"


class SelectedLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # optional
    selected_city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} selected {self.selected_city}"
