from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    ]