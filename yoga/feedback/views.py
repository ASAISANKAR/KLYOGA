from django.shortcuts import render
from .models import *
# Create your views here.
def feed(request):
    return render(request, 'feedback.html')

def feedbacksave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Comments = request.POST.get('Comments')
        Feedback.objects.create(name=name, email=email, Comments=Comments)
        return render(request,'homepage.html')
    return render(request, 'feedback.html')