from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #import module for handling http requests

def home(request):
    return HttpResponse('Hello, World!') #send http response with Hello World inside

#NOTE: This is just a function that can't do anything by itself, go to urls.py in myproject to see further steps