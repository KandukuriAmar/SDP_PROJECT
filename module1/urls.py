from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello1/', hello1, name='hello1'),
    path('', newhomepage, name='newhomepage'),
    path('travel/', travelpackage,name="travelpackage"),
    path('print/',print1,name="print"),
    path('printtoconsole/',printtoconsole,name='printtoconsole'),
    path('callrandomotp/',randomcall,name='randomcall'),
    path('printotpconsole/',randomotpgenerator,name='randomotpgenerator'),
    path('getdate/',getdate1,name='getdate1'),
    path('getmain/',getdate,name='getmain'),
    path('register/',registercall,name='registercall'),
    path('registerlogin/',registerlogin,name='registerlogin'),
    path('open_pie',open_pie,name='open_pie'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('takerentcar/',takerentcar,name='takerentcar'),
    path('feedback/',feedback,name='feedback'),
    path('mainfeedback/',mainfeedback,name='mainfeedback'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('signup/',signup,name='signup'),
    path('signup1/',signup1,name='signup1'),
]
