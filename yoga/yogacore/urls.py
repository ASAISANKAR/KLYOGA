from django.urls import path
from .views import *

urlpatterns = [

  path('',home,name='corehome'),
  path('log',core,name='core'),
  path('signkaro',signup,name='signup'),
  path('profile/',profile,name='profile'),
  path('update/',updateprofile,name='updateprofile'),
  path('logview/',logview,name='logview'),
  path('profileview/',profileview,name='profileview'),


]