from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    if request.GET:
        uid=request.GET.dict()['id'].upper()
        return redirect(f'/{uid}/view_details')
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
            return redirect(f'/{id}/home/')
        else:
            flag=False
    return render(request,'DigiResume/login.html',{'flag':flag})

def home(request,code):
    if sector is 1:
        x=Institution.objects.get(inst_code=code)
    elif sector is 2:
        x=Organisation.objects.get(org_code=code)        
    elif sector is 3:
        x=SevaStore.objects.get(sev_code=code)
    return render(request,'DigiResume/home.html',{'sector':sector,'x':x})

def register(request,code):
    return render(request,'DigiResume/register.html')

def add_course(request,code):
    return render(request,'DigiResume/add_course.html')

def add_work(request,code):
    return render(request,'DigiResume/add_work.html')

def history(request,code):
    return render(request,'DigiResume/history.html')

def activity(request,code):
    return render(request,'DigiResume/activity.html')

def view_details(request,uid):
    print(uid)
    # x=Person.objects.get(uid=uid)
    return render(request,'DigiResume/view_details.html')
