from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('register/<str:tier>/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('', include('index.urls')),
    path('', include('member.urls')),
    path('', include('event.urls'))
    ]
