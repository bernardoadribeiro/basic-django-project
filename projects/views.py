from django.shortcuts import render
from django.contrib import messages

from projects.models import Project
from .forms import ProjectForm

import markdown


#  Create your views here.
def index(request):
    projects = Project.objects.all()  # get all projects
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)


def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {
        'project': project,
        'project_description': markdown.markdown(project.description)
    }
    return render(request, 'project_detail.html', context)


def add_project(request):
    form = ProjectForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            # Get the variables values from POST request
            title = request.POST.get('title')
            description = request.POST.get('description')
            technology = request.POST.get('technology')
            image = request.POST.get('image')

            # Save the Project Object into the database using the inputed data from form.
            Project.objects.create(title=title, description=description, technology=technology,
                                   image=image)

            messages.success(request, 'Successfully added.')
        else:
            messages.error(request, 'Error while saving project info. Please try again later.')

    context = {
        'form': form,
        'form_title': 'New Project',
        'form_url': 'add_project'
    }
    return render(request, 'forms.html', context)
