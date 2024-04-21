from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User

def home(request):
    return render(request,'homepage.html')

def about(request):
    return render(request,'aboutus.html')

def login(request):
    return render(request, 'login.html')

def aech(request):
    vid1={'video': '/static/images/video.mp4'}
    return render(request, 'aech.html',vid1)



def custom_404(request, exception):
    return render(request, '404.html', status=404)



