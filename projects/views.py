from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projectsList = [

    {'id': '1', 'title': 'Ecommerce Website', 'description': 'Fully functional ecommerce website'},

    {'id': '2', 'title': 'Portfolio Website',
     'description': 'A personal website to write articles and display work'},

    {'id': '3', 'title': 'Social Network', 'description': 'An open source project built by the community'}

]


def projects(request):
    page = "Hello from Khalil Adib"
    number = 9
    context = {
        'page': page,
        'number': number,
        'projects': projectsList
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None

    for p in projectsList:
        if p['id'] == pk:
            projectObj = p

    context = {
        'project': projectObj
    }
    return render(request, 'projects/project.html', context)
