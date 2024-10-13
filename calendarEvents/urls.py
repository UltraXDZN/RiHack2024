from django.urls import path
from . import views

urlpatterns = [
    path('api/events/', views.get_events, name='get_events'),
    path('api/events/<int:event_id>/', views.get_event_detail, name='get_event_detail'),
    path('api/events/create/', views.create_event, name='create_event'),
    path('api/events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
