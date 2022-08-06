from .models import Person
from django import forms 

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Person
        fields=['name','aadhar','photo','dob','gender','street','district','state','pincode','email','mobile','nationality']

class AddCourseForm(forms.Form):
    choices=[
        ('class 10','class 10'),
        ('class 12','class 12')
        ]
    uid=forms.CharField(max_length=16)
    course_name=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    completion_date=forms.DateField()
    grade=forms.IntegerField()



class AddWorkForm(forms.Form):
    choices=[
        ('class 10','class 10'),
        ('class 12','class 12')
        ]
    uid=forms.CharField(max_length=16)
    role=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    join_date=forms.DateField()
    resign_date=forms.IntegerField()

class AddUnorganisedWorkForm(forms.Form):
    uid=forms.CharField(max_length=16)
    work_name=forms.CharField(max_length=16)
        