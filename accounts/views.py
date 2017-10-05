# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib import auth

# Create your views here.            


def login_view(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/sherpa/loggedin')
	else:
		return HttpResponseRedirect('/sherpa/invalid')


def loggedin_view(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_view(request):
	return render_to_response('invalid_login.html')


def logout_view(request):
	auth.logout(request)
	return render_to_response('logout.html')
