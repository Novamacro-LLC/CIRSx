from django.urls import path, include
from . import views
from index.views import stripe_events


urlpatterns = [
    path('', include('index.urls')),
    path('', include('member.urls')),
    path('events_register/', views.events_register, name='events_register'),
 #   path('guest_register/', views.guest_register, name='guest_register'),
    path('stripe_events/', stripe_events, name='stripe_events')
]
