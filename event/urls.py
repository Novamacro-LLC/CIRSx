from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('home.urls')),
    path('', include('member.urls')),
    path('events_register/', views.events_register, name='events_register'),
]
