import base64
from io import StringIO, BytesIO
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from collections import namedtuple
from .serializers import *
from .models import *
from .utilities import *
from .forms import *

# Create your views here.
#sector =1

#api 




class API(APIView):
    def get(self, request, uid):
        p = Person.objects.get(uid = uid)
        e = EducationInfo.objects.filter(uid=uid)
        wo = WorkInfoByOrganisation.objects.filter(uid=uid)
        wi = WorkInfoByInstitution.objects.filter(uid=uid)
        uw = UnorganisedWorkInfo.objects.filter(uid = uid)
        serializer ={ 'details': PersonSerializer(p).data , 'education' : EducationInfoSerializer(e, many=True).data, 'work ' : WorkInfoByInstitutionSerializer(wi, many=True).data + WorkInfoByOrganisationSerializer(wo, many=True).data }
        #serializer = EducationInfoSerializer(e, many=True)
        return Response(serializer)






#--------------------------------------------------------------------------------------------#


def index(request):
    if request.GET:
        uid=request.GET.dict()['id'].upper()
        return redirect(f'/{uid}/view_details')
    return render(request,'DigiResume/index.html')

def loginQR(request):
    uid = qrDetector()
    return redirect(f'/{uid}/view_details')



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
    if sector==1:
        x=Institution.objects.get(inst_code=code)
    elif sector==2:
        x=Organisation.objects.get(org_code=code)        
    elif sector==3:
        x=SevaStore.objects.get(seva_code=code)
    return render(request,'DigiResume/home.html',{'sector':sector,'code':code,'x':x})





def register(request,code):
    uid=generateUID()
    if uid in Person.objects.values_list('uid',flat=True):
        return register(request,code)

    if request.method == 'POST':
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.uid=uid
                obj.save()
                #card gen
                card=generateCard(uid)
                #card.show()

                buffer = StringIO()
                card.save(buffer, format='PNG')
                op = base64.b64encode(buffer.getvalue())
                #updating activity table
                InstitutionActivity(uid=Person(uid = uid), inst_code = Institution(inst_code=code), action = f'User resistered {uid}').save()
                return HttpResponse(f"""User resistered {uid}<br><a><img src="data:image/png;base64,{op}"/></a>""")
    else:
        form = RegisterForm()
    return render(request,'DigiResume/register.html',{'form':form,'sector':sector,'code':code})






def add_course(request,code):
    if request.method == 'POST':
            form = AddCourseForm(code, request.POST)
            if form.is_valid():
                obj = EducationInfo()
                uid = request.POST['uid']
                print(type(Person(uid=uid)))
                obj.uid = Person(uid = uid)
                obj.inst_code = Institution(inst_code=code)
                course_name = form.cleaned_data['course_name']
                obj.course_name = course_name
                obj.grade = form.cleaned_data['grade']
                obj.completion_date = form.cleaned_data['completion_date']
                obj.save()
                InstitutionActivity(uid=Person(uid = uid), inst_code = Institution(inst_code=code), action = f'{course_name} Course Added for {uid}').save()
                return HttpResponse(f'{course_name} Course Added for {uid}')


    else:
        form = AddCourseForm(code)  
    return render(request,'DigiResume/add_course.html',{'code':code,'sector':sector,'form':form})






def add_work(request,code):    
    if sector==1:    
        if request.method == 'POST':
            form = AddWorkInstitutionForm(code, request.POST)
            if form.is_valid():
                obj = WorkInfoByInstitution()
                uid = form.cleaned_data['uid']
                obj.uid = Person(uid = uid)
                obj.inst_code = Institution(inst_code=code)
                role = form.cleaned_data['role']
                obj.role = role
                obj.join_date = form.cleaned_data['join_date']
                obj.resign_date = None
                obj.save()
                InstitutionActivity(uid=Person(uid = Person(uid=uid)), inst_code = Institution(inst_code=code), action = f'{role} work Added for {uid}').save()
                return HttpResponse(f'{role} work Added for {uid}')


        else:
            form = AddWorkInstitutionForm(code)
            
    elif sector==2:
        if request.method == 'POST':
            form = AddWorkOrganisationForm(code, request.POST)
            if form.is_valid():
                obj = WorkInfoByOrganisation()
                uid = form.cleaned_data['uid']
                obj.uid = Person(uid = uid)
                obj.org_code = Organisation(org_code=code)
                role = form.cleaned_data['role']
                obj.role = role
                obj.join_date = form.cleaned_data['join_date']
                obj.resign_date = None
                obj.save()
                OrganisationActivity(uid=Person(uid = uid), org_code = Organisation(org_code=code), action = f'{role} work Added for {uid}').save()
                return HttpResponse(f'{role} work Added for {uid}')
   
        else:
            form = AddWorkOrganisationForm(code)

    elif sector==3:
        if request.method == 'POST':
            form = AddUnorganisedWorkForm(request.POST)
            if form.is_valid():
                # obj = UnorganisedWorkInfo()
                uid = form.cleaned_data['uid']
                # obj.uid = Person(uid = uid)
                # obj.seva_code = SevaStore(seva_code=code)
                work = form.cleaned_data['work_name']
                # obj.work_name = work
                # obj.save()
                SevaActivity(uid=Person(uid = uid), seva_code = SevaStore(seva_code=code), action = f'{work} work Added for {uid}').save()
                obj = form.save(commit = False)
                obj.seva_code = SevaStore(seva_code=code)
                obj.save()
                return HttpResponse(f'{work} work Added for {uid}')
        else:
            form = AddUnorganisedWorkForm()            
    return render(request,'DigiResume/add_work.html',{'code':code,'form':form, 'sector':sector})






def add_resign(request,code):
    if request.GET:
        uid= request.GET.dict()['uid']
        o = WorkInfoByInstitution.objects.get(uid= uid, inst_code = code)
        name = o.name
        if sector==1:
            o = WorkInfoByInstitution.objects.get(uid= uid, inst_code = code)
            o.resign_date = request.GET.dict()['resign_date']
            o.save()
            InstitutionActivity(uid=Person(uid = Person(uid=uid)), inst_code = Institution(inst_code=code), action = f'{o.role} resign date Added for {uid}').save()
            return HttpResponse(f'{o.role} resign date Added for {uid}')

        elif sector==2:
            o = WorkInfoByOrganisation.objects.get(uid= uid, org_code = code)
            o.resign_date = request.GET.dict()['resign_date']
            o.save()
            OrganisationActivity(uid=Person(uid = uid), org_code = Organisation(org_code=code), action = f'{o.role} resign date Added for {uid}').save()
            return HttpResponse(f'{o.role} resign date Added for {uid}')
    else:
        o=''

    return render(request,'DigiResume/add_resign.html',{'code':code,'o':o, 'sector':sector})





def activity(request,code):
    if sector==1:
        o=InstitutionActivity.objects.filter(inst_code=code)
    if sector==2:
        o=OrganisationActivity.objects.filter(org_code=code)
    if sector==3:
        o=SevaActivity.objects.filter(seva_code=code)
    return render(request,'DigiResume/activity.html',{'code':code, 'o':o, 'sector':sector})





def view_details(request,uid):
    x=Person.objects.get(uid=uid)
    y=EducationInfo.objects.filter(uid=uid)
    z=WorkInfoByOrganisation.objects.filter(uid=uid)
    a = WorkInfoByInstitution.objects.filter(uid=uid)
    uw = UnorganisedWorkInfo.objects.filter(uid = uid)
    return render(request,'DigiResume/view_details.html',{'x':x,'y':y,'z':z,'a':a, 'uw':uw})
