from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('about_us/', views.about_us, name='about_us'),
    path('conference/<str:name>/', views.conference, name='conference'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('medical_glossary/', views.medical_glossary, name='medical_glossary'),
    path('environmental_glossary/', views.environmental_glossary, name='environmental_glossary'),
    path('speakers/', views.speakers, name='speakers'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('shoey/', views.shoey, name='shoey'),
    path('stripe_pro/', views.stripe_pro, name='stripe_pro'),
    path('stripe_patient/', views.stripe_patient, name='stripe_patient'),
    path('stripe_events/', views.stripe_events, name='stripe_events'),
    path('placeholder/', views.placeholder, name='placeholder'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

