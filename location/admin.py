from django.contrib import admin
from .models import County, City, SelectedLocation

admin.site.register(County)
admin.site.register(City)
admin.site.register(SelectedLocation)

