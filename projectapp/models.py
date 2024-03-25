from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_image_1 = models.ImageField(upload_to='project_images')
    project_image_2 = models.ImageField(upload_to='project_images')
    technology_used = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos', blank=True)
    github_link = models.URLField(blank=True)
    features = models.TextField()
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    project_heading = models.CharField(max_length=200)
    working = models.TextField()

    def __str__(self):
        return self.project_name
