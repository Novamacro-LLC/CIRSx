from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('register/<str:tier>/', views.register, name='register'),
    path('register_test/<str:tier>/', views.register, name='test'),
    path('login/', views.login_user, name='login'),
    path('', include('home.urls')),
    path('', include('member.urls'))
    ]
