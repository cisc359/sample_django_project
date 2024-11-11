

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='weather'),
    path('weather_details/', views.weather_details ),
]

