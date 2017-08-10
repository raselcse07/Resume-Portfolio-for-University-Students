from django.contrib import admin
from .models import (UploadCV,
                    AdditionalInfo,
                    Portfolio,
                    TechnicalSkills,
                    Education,
                    WorkHistory,
                    Service,
                    Succeess,
                    WorkingProcess,
                    Clients)

class AdditionalInfoModelAdmin(admin.ModelAdmin):

    list_display=["full_name","user","email","cell_number"]
    list_display_links=["full_name"]
    list_filter=["full_name","user","email","cell_number"]

    class Meta:
        model=AdditionalInfo

class ClientsModelAdmin(admin.ModelAdmin):

    list_display=["user","name_of_clients"]
    list_display_links=["user"]
    list_filter=["user","name_of_clients"]

    class Meta:
        model=Clients

class EducationModelAdmin(admin.ModelAdmin):

    list_display=["user","institute_name","degree","passing_year"]
    list_display_links=["user"]
    list_filter=["user","institute_name","degree","passing_year"]

    class Meta:
        model=Education

class PortfolioModelAdmin(admin.ModelAdmin):

    list_display=["user","project_name","project_type","project_url"]
    list_display_links=["user"]
    list_filter=["user","project_name","project_type","project_url"]

    class Meta:
        model=Portfolio

class ServiceModelAdmin(admin.ModelAdmin):

    list_display=["user","service_type"]
    list_display_links=["user"]
    list_filter=["user","service_type"]

    class Meta:
        model=Service

class SuccessModelAdmin(admin.ModelAdmin):

    list_display=["user","total_complete_project","total_happy_clients","awards_won","total_ongoing_project"]
    list_display_links=["user"]
    list_filter=["user"]

    class Meta:
        model=Succeess

class TechnicalSkillsModelAdmin(admin.ModelAdmin):

    list_display=["user","skills","skill_level"]
    list_display_links=["user"]
    list_filter=["user"]

    class Meta:
        model=TechnicalSkills


class UploadResumesModelAdmin(admin.ModelAdmin):

    list_display=["user","is_publish"]
    list_display_links=["user"]
    list_filter=["user"]

    class Meta:
        model=UploadCV

class WorkHistoryModelAdmin(admin.ModelAdmin):

    list_display=["user","company_name","position","start_date","end_date"]
    list_display_links=["user"]
    list_filter=["user"]

    class Meta:
        model=WorkHistory

class WorkingProcessModelAdmin(admin.ModelAdmin):

    list_display=["user","title"]
    list_display_links=["user"]
    list_filter=["user"]

    class Meta:
        model=WorkingProcess


admin.site.register(UploadCV,UploadResumesModelAdmin)
admin.site.register(AdditionalInfo,AdditionalInfoModelAdmin)
admin.site.register(Portfolio,PortfolioModelAdmin)

admin.site.register(TechnicalSkills,TechnicalSkillsModelAdmin)
admin.site.register(Education,EducationModelAdmin)
admin.site.register(WorkHistory,WorkHistoryModelAdmin)


admin.site.register(Service,ServiceModelAdmin)
admin.site.register(Succeess,SuccessModelAdmin)
admin.site.register(WorkingProcess,WorkingProcessModelAdmin)
admin.site.register(Clients,ClientsModelAdmin)
