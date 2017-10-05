# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location
from .forms import UserLoginForm

# Create your views here.


def index_view(request):
    context = {
    
    }
    return render(request, 'index.html', context)


#                #
# Location Views #
#                #

                
def add_view(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        location = Location(title=title, text=text)
        location.save()

        return redirect('/sherpa')
    else:
        return render(request, 'add.html')

def details_view(request, id):
    location = Location.objects.get(id=id)
    context = {
        'location': location
    }
    return render(request, 'details.html', context)

def location_list_view(request):
    locations = Location.objects.all()[:10]
    context = {
        'locations': locations
    }   
    return render(request, 'location_list.html', context)
