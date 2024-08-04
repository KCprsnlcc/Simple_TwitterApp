# twitter_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_status/', views.post_status, name='post_status'),
    path('check_profanity/', views.check_profanity, name='check_profanity'),
]
