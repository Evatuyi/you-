# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location

# Create your views here.


def index(request):
    locations = Location.objects.all()[:10]
    context = {
        'locations': locations
    }
    return render(request, 'index.html', context)


def details(request, id):
    location = Location.objects.get(id=id)
    context = {
        'location': location
    }
    return render(request, 'details.html', context)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        location = Location(title=title, text=text)
        location.save()

        return redirect('/sherpa')
    else:
        return render(request, 'add.html')
