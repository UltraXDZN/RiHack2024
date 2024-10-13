from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('news/', views.news_view, name='news'),
    path('calendar/', views.calendar_view, name='calendar'),

    # API calls
    path('', include('news.urls')),
    path('', include('sim.urls')),
    path('', include('calendarEvents.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
