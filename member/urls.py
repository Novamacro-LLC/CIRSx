from django.urls import path
from . import views

urlpatterns = [
path('tier_welcome/', views.tier_welcome, name='tier_welcome'),
path('tier_videos/', views.tier_videos, name='tier_videos')

]