from django.shortcuts import render
from projects.models import Project


# Create your views here.
def index(request):
    projects = Project.objects.all()  # get all projects
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)


def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
