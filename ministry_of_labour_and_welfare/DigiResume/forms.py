from .models import Person,EducationInfo,WorkInfoByOrganisation,WorkInfoByInstitution,UnorganisedWorkInfo,courses
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Person
        fields=['name','aadhar','photo','dob','gender','district','state','pincode','email','mobile','nationality']
        widgets = {
            'gender':forms.RadioSelect(choices=[
                ('Male','Male'),
                ('Female','Female'),
                ('Other','Other')
            ])
        }



class AddCourseForm(forms.ModelForm):
    uid=forms.CharField(max_length=16)
    choices=[
        ('class 10','class 10'),
        ]
    class Meta:
        model = EducationInfo
        exclude = ['inst_code']


        



class AddWorkOrganisationForm(forms.ModelForm):
    choices=[
        ('class 10','class 10'),
        ('class 12','class 12')
        ]
    class Meta:
        model = WorkInfoByOrganisation
        exclude = ['org_code']


class AddWorkInstitutionForm(forms.ModelForm):
    choices=[
        ('class 10','class 10'),
        ('class 12','class 12')
        ]
    class Meta:
        model = WorkInfoByInstitution
        exclude = ['inst_code']

class AddUnorganisedWorkForm(forms.ModelForm):
    class Meta:
        model = UnorganisedWorkInfo
        exclude = ['seva_code']
        