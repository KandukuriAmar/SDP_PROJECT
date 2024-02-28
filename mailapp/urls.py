from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('sendemail/',send_emails,name='send_emails'),
]