from django.urls import path
from . import views

urlpatterns = [
    path('',views.lp),
    path('home/', views.home),
    path('wildlife/', views.wildflife),
    path('forest/', views.forest),
    path('visitors/', views.visitors),
    path('logistics/', views.logistics),
]