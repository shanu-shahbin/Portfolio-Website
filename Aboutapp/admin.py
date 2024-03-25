from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Experience, Services

admin.site.register(Experience)
admin.site.register(Services)
