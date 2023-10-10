from django.urls import path
from . import views

# list of path and there renders
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]
