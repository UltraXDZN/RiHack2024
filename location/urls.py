from django.urls import path
from . import views

urlpatterns = [
    path('api/locations/', views.get_locations, name='get_locations'),
    path('api/locations/set/', views.set_locations, name='set_locations'),
    path('api/locations/selected/', views.get_selected_locations, name='get_selected_locations'),
]
