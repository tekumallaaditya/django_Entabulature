from django.shortcuts import render
from django.http import HttpResponse
from .models import homeDB, projectsDB, constructionPicsDB, elevationPicsDB, interiorPicsDB, teamDB, blogDB, testimonialDB
from home.forms import testimonialForm

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

def constructionPics(request):
    pics = constructionPicsDB.objects.all()

    context = {
        'pics': pics
    }

    return render(request, 'home/constructionPics.html', context)

def elevationPics(request):
    pics = elevationPicsDB.objects.all()

    context = {
        'pics': pics
    }

    return render(request, 'home/elevationPics.html', context)

def interiorPics(request):
    pics = interiorPicsDB.objects.all()

    context = {
        'pics': pics
    }

    return render(request, 'home/interiorPics.html', context)

def team(request):
    members = teamDB.objects.all()

    context = {
        'members': members
    }

    return render(request, 'home/team.html', context)

def blog(request):
    blogs = blogDB.objects.all()

    context = {
        'blogs': blogs
    }

    return render(request, 'home/blog.html', context)

def testimonials(request):
    template_name = 'home/testimonial.html'
    testimonials = testimonialDB.objects.all()
    if request.method == 'GET':
        form = testimonialForm()
    else:
        form = testimonialForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, template_name, {'form': form, 'testimonials': testimonials})


