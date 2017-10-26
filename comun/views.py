# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Home(request):
	return render(request, "index.html")

@csrf_exempt
def login_view(request):
    mensaje = ""
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje = 'Ok'
        else:
            mensaje = 'Nombre de usuario o clave invalido'

    return JsonResponse({'mensaje':mensaje})

@csrf_exempt
def logout_view(request):
    logout(request)

    print("test12")
    return JsonResponse({'mensaje': 'Oki'})

@csrf_exempt
def logged_view(request):
    if request.user.is_authenticated():
        mensaje = 'Ok '+str(request.user.username)
    else:
        mensaje = 'No'
    return JsonResponse({'mensaje':mensaje})