from django.urls import path
from .views import *

urlpatterns = [

  path('',home,name='corehome'),
  path('log',core,name='core'),
  path('signkaro',signup,name='signup'),
  path('profile/',profile,name='profile'),
]