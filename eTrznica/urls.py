from django.urls import path
from . import views

urlpatterns = [
    path('api/ads/', views.list_posts, name='list_posts'),
    path('api/ads/create/', views.create_post, name='create_post'),
    path('api/ads/<int:ad_id>/edit/', views.edit_post, name='edit_post'),
    path('api/ads/<int:ad_id>/delete/', views.delete_post, name='delete_post'),
]
