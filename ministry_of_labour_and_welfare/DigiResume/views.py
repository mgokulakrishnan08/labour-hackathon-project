import base64
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *
from PIL import Image
from django.core.files.storage import default_storage
from .utilities import *
from io import BytesIO
from .forms import *


# from .utilities import *

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
            x=Organisation.objects.get(org_code=id).password
        elif 'SEV' in id:
            sector=3
            x=SevaStore.objects.get(seva_code=id).password
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
        x=SevaStore.objects.get(seva_code=code)
    return render(request,'DigiResume/home.html',{'sector':sector,'code':code,'x':x,})

def register(request,code):
    uid=generateUID()
    name='selva geetha'
    dob='21-02-2002'
    gender='female'
    info=f'Name:{name}\nDOB:{dob}\nGender:{gender}'
    card=generateCard(uid,info)
    # card.show()
   
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
            
                return redirect('/thanks/')
    else:
        form = RegisterForm()
    return render(request,'DigiResume/register.html',{'form':form,'sector':sector,'code':code})

def add_course(request,code):
    if request.method == 'POST':
            form = AddCourseForm(request.POST)
            if form.is_valid():
            
                return redirect('/thanks/')
    else:
        form = AddCourseForm()  
    return render(request,'DigiResume/add_course.html',{'code':code,'sector':sector,'form':form})

def add_work(request,code):
    if sector==2:
        if request.method == 'POST':
            form = AddWorkForm(request.POST)
            if form.is_valid():
                return redirect('/thanks/')
        else:
            form = AddWorkForm()
    elif sector==3:
        if request.method == 'POST':
            form = AddUnorganisedWorkForm(request.POST)
            if form.is_valid():
                return redirect('/thanks/')
        else:
            form = AddUnorganisedWorkForm()            
    return render(request,'DigiResume/add_work.html',{'code':code,'form':form})


def activity(request,code):
    return render(request,'DigiResume/activity.html',{'code':code})

def view_details(request,uid):
    x=Person.objects.get(uid=uid)
    return render(request,'DigiResume/view_details.html',{'x':x})
