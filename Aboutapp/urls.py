from django.urls import path

from Aboutapp import views


app_name = 'aboutApp'
urlpatterns = [
    path('', views.About, name="about"),
]