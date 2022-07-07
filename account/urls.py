from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('register/path converter: tier', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('', include('home.urls')),
    ]
