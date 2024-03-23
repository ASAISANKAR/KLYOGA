from django.shortcuts import render
from .models import *
# Create your views here.
def feed(request):
    return render(request, 'feedback.html')

def feedbacksave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id=request.POST.get('id')
        email = request.POST.get('email')
        gender=request.POST.get('gender')
        phonenumber=request.POST.get('phonenumber')
        branch=request.POST.get('branch')
        Comments = request.POST.get('comments')
        Feed.objects.create(name=name, email=email, gender=gender,phonenumber=phonenumber, branch=branch,iid=id,Comments=Comments)
        return render(request,'homepage.html')
    return render(request, 'feedback.html')