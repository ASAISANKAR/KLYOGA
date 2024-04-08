from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

from .models import *


# Create your views here.

@login_required(login_url='core')
def home(request):
    return render(request, 'corehp.html')

import datetime
import pytz

def core(request):
    if request.method=='POST':
        username=request.POST['name']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            # India Time
            utc_now = datetime.datetime.utcnow()
            india_timezone = pytz.timezone('Asia/Kolkata')
            india_time = utc_now.replace(tzinfo=pytz.utc).astimezone(india_timezone)
            india_date = india_time.date()
            Login.objects.create(username=username, password=pass1,date=india_date)
            return redirect('corehome')

        else:
            return HttpResponse("Invalid Credentials")

    else:
        return render(request,'login.html')

@login_required(login_url='core')
def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("username already exist")
        else:
            user=User.objects.create_user(username=username,password=pass1)
            user.save()
            Signup.objects.create(username=username,password=pass1)
            return HttpResponse("Account Created Successfully")

    return render(request,'signup.html')




def profile(request):

    return render(request,'profile.html')