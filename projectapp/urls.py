from django.urls import path
from . import views
from .views import Projects, project_details

app_name = 'ProjectsApp'
urlpatterns = [
    path('', views.Projects, name="Projects"),
    path('project/<int:project_id>/', views.project_details, name="project_details"),
]
