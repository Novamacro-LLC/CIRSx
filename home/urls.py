from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('about_us/', views.about_us, name='about_us'),
    path('conference/', views.conference, name='conference'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('medical_glossary/', views.medical_glossary, name='medical_glossary'),
    path('environmental_glossary/', views.environmental_glossary, name='environmental_glossary'),
    path('speakers/', views.speakers, name='speakers'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('shoey/', views.shoey, name='shoey'),

]
