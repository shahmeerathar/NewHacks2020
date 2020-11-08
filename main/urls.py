from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('main/', views.main, name='main'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
