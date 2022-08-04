from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(Person)
admin.site.register(Institution)
admin.site.register(courses)
admin.site.register(RolesByInstitution)
admin.site.register(InstitutionRequest)
admin.site.register(InstitutionHistory)
admin.site.register(Organisation)
admin.site.register(RolesByOrganisation)
admin.site.register(OrganisationRequest)
admin.site.register(OrganisationHistory)
admin.site.register(SevaStore)
admin.site.register(SevaRequest)
admin.site.register(SevaHistory)
admin.site.register(EducationInfo)
admin.site.register(WorkInfoByOrganisation)
admin.site.register(WorkInfoByInstitution)
admin.site.register(UnorganisedWorkInfo)