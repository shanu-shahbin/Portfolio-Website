from django.shortcuts import render
from .models import Experience, Services

def About(request):
    experiences = Experience.objects.all()
    services = Services.objects.all()
    context = {
        'experiences': experiences,
        'services': services
    }
    return render(request, 'about.html', context)
