from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('',feed,name='feed'),
    path('feedbacksave/',feedbacksave,name='feedbacksave'),
    path('viewfeed/',viewfeed,name='viewfeed'),



]
