from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('index.urls')),
    path('', include('member.urls')),
    path('events_register/', views.events_register, name='events_register'),
    path('guest_register/', views.guest_register, name='guest_register'),
]
