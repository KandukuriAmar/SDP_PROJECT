import random
import string
from django.shortcuts import *
from . forms import *
from django.http import HttpResponse
import datetime
from .models import *
import matplotlib.pyplot as plt
import numpy as np

# from numpy import long


# Create your views here.

# def hello(request):
#     return render(request,)

def hello1(request):
    return HttpResponse("<center>Welcome To Travel Management HomePage</center>")

def newhomepage(request):
    return render(request,'NewHome.html')

def travelpackage(request):
    return render(request, "Travelpackage.html")

def print1(request):
    return render(request,'PrintToConsole.html')

def printtoconsole(request):
    userinput = None
    if request.method == "POST":
        userinput = request.POST.get('userinput', '')
        print(f"User Input: {userinput}")

    a1 = {'userinput': userinput}
    print(a1)
    return render(request, 'PrintToConsole.html', a1)

def randomcall(request):
    return render(request,'RandomOTPgenerator.html')

def randomotpgenerator(request):
    userinput = None
    if request.method == "POST":
        userinput = request.POST.get('userinput', '')
        print(f"User Input: {userinput}")

    a2=int(userinput)
    ran1=''.join(random.sample(string.digits,k=a2))

    a2 = {'ran1': ran1}
    print(a2)
    return render(request, 'RandomOTPgenerator.html', a2)

def getdate1(request):
    return render(request,'Getdate.html')

from django.shortcuts import render
def getdate(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'Getdate.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()

    return render(request, 'Getdate.html', {'form': form})

def registercall(request):
    return render(request,'Register.html')

def registerlogin(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Amar.objects.filter(email=email).exists():
            return HttpResponse("Email is already Registered Please try with another Email")

        Amar.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'Register.html')


def open_pie(request):
    return render(request,'chart_form.html')

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})

def takerentcar(request):
    return render(request,'Takerentcar.html')

def feedback(request):
    return render(request,'Feedback.html')
from django.core.mail import send_mail
def mainfeedback(request):
    if request.method=="POST":
        FirstName=request.POST.get('FirstName')
        LastName=request.POST.get('LastName')
        Email=request.POST.get('Email')
        Comment=request.POST.get('Comment')

        Feedback.objects.create(FirstName=FirstName,LastName=LastName,Email=Email,Comment=Comment)
        send_mail(
            'Thank you for your feedback',
            '2200030959cseh@gmail.com',
            Comment,
            [Email],
            fail_silently=False,
        )
    return HttpResponse("<h3><center>Mail Sent sucessfully<center><h3>")
        #return redirect('newhomepage')
    #return render(request,'Feedback.html')

# def login(request):
#     return render(request,'Login.html')

from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'Login.html')

def signup(request):
    return render(request,'SignUp.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewHome.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'Homepage.html')
