# main/urls.py

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'), 
    path('acoes/<int:pk>/', views.action_detail, name='action_detail'), 
    path('eventos/<int:pk>/', views.event_detail, name='event_detail'),
]
    
