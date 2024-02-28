from django.shortcuts import render
import csv
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def send_emails(request):
    csv_file_path = r'C:\Users\kandu\Desktop\All sub\PFSD\DjangoProjects\TravelManagment\static\mailfile.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                '2200030959cseh@gmail.com',     
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'EmailSend.html')


def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment+"-------------------------This is comment"
        data=contactUs(firstname=firstname,lastname=lastname,email=email)
        data.save()