from django.shortcuts import render
from.models import Project
from django.shortcuts import get_object_or_404

def Projects(request):
    projects = Project.objects.all()
    context = {
        'project_list': projects
    }
    return render(request, 'projects.html', context)

def project_details(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project_details.html", {'project': project})
