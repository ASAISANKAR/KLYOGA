from django.shortcuts import render
from .models import *
# Create your views here.
def feed(request):
    return render(request, 'feedback.html')

import datetime
import pytz
def feedbacksave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id=request.POST.get('id')
        email = request.POST.get('email')
        gender=request.POST.get('gender')
        phonenumber=request.POST.get('phonenumber')
        branch=request.POST.get('branch')
        Comments = request.POST.get('comments')
        #India Time
        utc_now = datetime.datetime.utcnow()
        india_timezone = pytz.timezone('Asia/Kolkata')
        india_time = utc_now.replace(tzinfo=pytz.utc).astimezone(india_timezone)
        india_date = india_time.date()
        Feed.objects.create(name=name, email=email, gender=gender,phonenumber=phonenumber, branch=branch,iid=id,Comments=Comments,date=india_date)
        return render(request,'homepage.html')
    return render(request, 'feedback.html')

def viewfeed(request):
    job_details_list = Feed.objects.all()
    return render(request, 'viewfeed.html', {'job_details_list': job_details_list})


