from django.urls import path

from homeApp import views

app_name = 'homeApp'
urlpatterns = [
    path('', views.home, name="home")
]