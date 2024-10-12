from django.urls import path
from . import views

urlpatterns = [
    path('api/news/', views.get_news, name='get_news'),
    path('api/news/<int:news_id>/', views.get_news_detail, name='get_news_detail'),
    path('api/news/create/', views.create_news, name='create_news'),
    path('api/news/delete/<int:news_id>/', views.delete_news, name='delete_news'),
]