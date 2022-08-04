from django.db import models

# Create your models here.

#-----------------------------------------------------------------------#

#person table

class Person(models.Model):
    uid=models.CharField(max_length=16,primary_key=True)
    name=models.CharField(max_length=50)
    aadhar=models.IntegerField()
    photo=models.ImageField(upload_to=f'photos/{name}')
    dob=models.DateField()
    gender=models.CharField(max_length=6)
    street=models.CharField(max_length=50)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    email=models.CharField(max_length=30)
    mobile=models.IntegerField()
    nationality=models.CharField(max_length=10)
#-----------------------------------------------------------------------#
#institution tables
class Institution(models.Model):
    inst_code=models.CharField(max_length=9,primary_key=True)
    password=models.CharField(max_length=16)
    owner_name=models.CharField(max_length=50)
    owner_uid=models.CharField(max_length=16)
    street=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    email=models.CharField(max_length=30)
    mobile=models.IntegerField()

class courses(models.Model):
    inst_code=models.ForeignKey(Institution,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=20)

class RolesByInstitution(models.Model):
    inst_code=models.ForeignKey(Institution,on_delete=models.CASCADE)
    role_name=models.CharField(max_length=20)

class InstitutionRequest(models.Model):
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    inst_code=models.ForeignKey(Institution,on_delete=models.CASCADE)
    status=models.CharField(max_length=7)

class InstitutionHistory(models.Model):
    date_time=models.DateTimeField(auto_now=True)
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    inst_code=models.ForeignKey(Institution,on_delete=models.CASCADE)
    action=models.CharField(max_length=50)
    

#-----------------------------------------------------------------------#
#oraganisation tables
class Organisation(models.Model):
    org_code=models.CharField(max_length=9,primary_key=True)
    password=models.CharField(max_length=16)
    owner_name=models.CharField(max_length=50)
    owner_uid=models.CharField(max_length=16)
    street=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    email=models.CharField(max_length=30)
    mobile=models.IntegerField()

class RolesByOrganisation(models.Model):
    org_code=models.ForeignKey(Organisation,on_delete=models.CASCADE)
    role_name=models.CharField(max_length=20)

class OrganisationRequest(models.Model):
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    org_code=models.ForeignKey(Organisation,on_delete=models.CASCADE)
    status=models.CharField(max_length=7)

class OrganisationHistory(models.Model):
    date_time=models.DateTimeField(auto_now=True)
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    org_code=models.ForeignKey(Organisation,on_delete=models.CASCADE)
    action=models.CharField(max_length=50)

#-----------------------------------------------------------------------#
#seva stores for unorganised works
class SevaStore(models.Model):
    seva_code=models.CharField(max_length=9,primary_key=True)
    password=models.CharField(max_length=16)
    owner_name=models.CharField(max_length=30)
    owner_uid=models.CharField(max_length=16)
    street=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    email=models.CharField(max_length=20)
    mobile=models.IntegerField()

class SevaRequest(models.Model):
    uid=models.ForeignKey(Person ,on_delete=models.CASCADE)
    seva_code=models.ForeignKey(SevaStore ,on_delete=models.CASCADE)
    status=models.CharField(max_length=7)

class SevaHistory(models.Model):
    date=models.DateField(auto_now=True)
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    seva_code=models.ForeignKey(SevaStore ,on_delete=models.CASCADE)
    action=models.CharField(max_length=50)


#-----------------------------------------------------------------------#

#person information

class EducationInfo(models.Model):
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    inst_code=models.ForeignKey(Institution,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=20)
    completion_date=models.DateField()
    grade=models.IntegerField()

class WorkInfoByOrganisation(models.Model):
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    org_code=models.ForeignKey(Organisation,on_delete=models.CASCADE)
    role=models.CharField(max_length=20)
    join_date=models.DateField()
    resign_date=models.DateField()

class WorkInfoByInstitution(models.Model):
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    inst_code=models.ForeignKey(Institution,on_delete=models.CASCADE)
    role=models.CharField(max_length=20)
    join_date=models.DateField()
    resign_date=models.DateField()

class UnorganisedWorkInfo(models.Model):
    uid=models.ForeignKey(Person,on_delete=models.CASCADE)
    seva_code=models.ForeignKey(SevaStore,on_delete=models.CASCADE)
    work_name=models.CharField(max_length=20)

#-----------------------------------------------------------------------#


