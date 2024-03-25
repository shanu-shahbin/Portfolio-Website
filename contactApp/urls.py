from django.urls import path

from contactApp import views


app_name = 'contactApp'
urlpatterns = [
    path('', views.Contact, name="Contact"),
]