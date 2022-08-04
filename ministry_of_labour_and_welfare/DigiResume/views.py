from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return render(request,'DigiResume/index.html')

def login(request):
    return render(request,'DigiResume/login.html')

def home(request):
    return render(request,'DigiResume/home.html')

def register(request):
    return render(request,'DigiResume/register.html')

def add_course(request):
    return render(request,'DigiResume/add_course.html')

def add_work(request):
    return render(request,'DigiResume/add_work.html')

def history(request):
    return render(request,'DigiResume/history.html')

def activity(request):
    return render(request,'DigiResume/activity.html')

def view_details(request):
    return render(request,'DigiResume/view_details.html')
