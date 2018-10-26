from django.shortcuts import render
from django.http import HttpResponse
from .models import homeDB

def home(request):
    pics = homeDB.objects.all()[:10]
    context = {
        'title': 'test',
        'pics': pics
    }

    return render(request, 'home/main.html', context)
    #return HttpResponse('home page works!')