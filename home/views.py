from django.shortcuts import render
from django.http import HttpResponse
from .models import homeDB, projectsDB

def home(request):
    pics = homeDB.objects.all()[:13]
    images = []
    for each in pics:
        images.append(each.thumb)
    context = {
        'title': 'test',
        'pics': pics,
        'images': images
    }

    return render(request, 'home/main.html', context)
    #return HttpResponse('home page works!')

def projectPage(request):
    projects = projectsDB.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'home/projects.html', context)