from django.urls import path, include
from . import views

urlpatterns = [
    path('tier_welcome/', views.tier_welcome, name='tier_welcome'),
    path('tier_videos/', views.tier_videos, name='tier_videos'),
    path('bibliographies/', views.bibliographies, name='bibliographies'),
    path('research_papers/', views.research_papers, name='research_papers'),
    path('', include('index.urls')),
    path('past_events/', views.past_events, name='past_events'),
    path('archived_events/<str:name>/', views.archived_events, name='archived_events'),
    path('doc_route/<str:name>/', views.doc_route, name='doc_route'),
    path('search/', views.doc_search, name='search'),


]