from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('artii/', views.artii),
    path('result/', views.result),
    path('push/', views.push),
    path('pull/', views.pull)
]