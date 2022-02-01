from django.urls import path
from . import views

# 
urlpatterns = [
  path('', views.challenge_welcome),
  path('submit/', views.challenge_submit)
]