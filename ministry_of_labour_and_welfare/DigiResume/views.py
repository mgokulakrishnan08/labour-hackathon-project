from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    if request.GET:
        id=request.GET.dict()['id'].upper()
        return redirect('/view_details/')
    return render(request,'DigiResume/index.html')

def login(request):
    flag=True
    if request.GET:
        id=request.GET.dict()['id'].upper()
        password=request.GET.dict()['password']
        global sector
        if 'EDU' in id:
            sector=1
            x=Institution.objects.get(inst_code=id).password
        elif 'ORG' in id:
            sector=2
            x=Institution.objects.get(org_code=id).password
        elif 'SEV' in id:
            sector=3
            x=Institution.objects.get(sev_code=id).password
        if password==x:
            return redirect('/home/')
        else:
            flag=False
    return render(request,'DigiResume/login.html',{'flag':flag})

def home(request):
    return render(request,'DigiResume/home.html',{'sector':sector})

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
