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
        details = User.objects.get(username=username)
        print(details.password)

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
            if Profile.objects.filter(username=username).exists():
                return HttpResponse("username already exist")
            else:
                Profile.objects.create(username=username)

        else:
            user=User.objects.create_user(username=username,password=pass1)
            user.save()
            Signup.objects.create(username=username,password=pass1)
            Profile.objects.create(username=username)
            return HttpResponse("Account Created Successfully")

    return render(request,'signup.html')




def profile(request):
    if Profile.objects.filter(username=request.user).exists():
        coredetails = Profile.objects.get(username=request.user)
        return render(request, 'profile.html', {'coredetails':coredetails})
    else:
        return HttpResponse("Profile Does not Exist")

def updateprofile(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        idnumber = request.POST['idnumber']
        branch = request.POST['branch']
        college = request.POST['college']
        image = request.POST['image']

        userprofile = Profile.objects.get(username=request.user)

        userprofile.name = name
        userprofile.email = email
        userprofile.phonenumber = phonenumber
        userprofile.idnumber = idnumber
        userprofile.branch = branch
        userprofile.college = college
        userprofile.image = image

        # Save the updated profile
        userprofile.save()
        return redirect('profile')
    return redirect(profile)

def logview(request):
    details=Login.objects.all()
    return render(request,'logindetails.html',{'details':details})

def profileview(request):
    details=Profile.objects.all()
    return render(request,'coredata.html',{'details':details})



