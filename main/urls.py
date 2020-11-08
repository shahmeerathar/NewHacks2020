from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='room'),
    path('user/', views.user, name='user'),
    path('main/', views.main, name='main'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
