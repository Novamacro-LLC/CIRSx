from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('about_us/', views.about_us, name='about_us'),
    path('conference/', views.conference, name='conference')
]
