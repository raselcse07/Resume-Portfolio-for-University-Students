from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse,Http404
from Academic.models import Department
from Users.models import Profile
from .models import (
                    UploadCV,
                    AdditionalInfo,
                    Portfolio,
                    TechnicalSkills,
                    Education,
                    WorkHistory,
                    Service,
                    Succeess,
                    WorkingProcess,
                    Clients
                    )

from .forms import (
                    AdditinalInfoCreationForm,
                    ResumeUploadForm,
                    PortfolioForm,
                    TechnicalSkillCreateForm,
                    EducationalInfoForm,
                    WorkHistoryForm,
                    ServiceCreationForm,
                    SuccessCreationForm,
                    WorkingProcessCreationForm,
                    ClientsCreationForm
                    )



def PreviewCV(request,dept_name=None,dept_session=None,reg_number=None):

    dept_name   =Department.objects.get(dept_name_short=dept_name)

    try:
        if dept_name:

            qs=Profile.objects.get(dept_name=dept_name,academic_year=dept_session,reg_number=reg_number)
            cv=UploadCV.objects.get(user=qs.user)

        template_name="cv_portfolio/cv.html"
        context={"cv":cv,"qs":qs}

        return render(request,template_name,context)
    except:
        return render(request,"cv_portfolio/cv_not_found.html")

# Create Additional Information

def CreateAdditionalInfo(request):

    user_exists=AdditionalInfo.objects.filter(user=request.user).exists()
    form=AdditinalInfoCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        if not user_exists:
            instance.save()
            messages.success(request, "Successfully Added Additional Informations")
            return HttpResponseRedirect("/students/profile")
        else:
            return render(request,"cv_portfolio/exists.html",{})

    template_name="cv_portfolio/create_additional_info.html"
    context={"form":form}

    return render(request,template_name,context)

# Update Additional Informations

def UpdateAdditionalInfo(request):

    instance=AdditionalInfo.objects.get(user=request.user)
    form=AdditinalInfoCreationForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Additional Informations")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_additional_info.html"
    context={"form":form}

    return render(request,template_name,context)

# Create Skills

def CreateTechnicalSkill(request):

    form=TechnicalSkillCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Created Technical Skills")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_skill.html"
    context={"form":form}

    return render(request,template_name,context)

# Skill Lists

def SkillList(request):

    qs=TechnicalSkills.objects.filter(user=request.user)
    template_name="cv_portfolio/skill_list.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Skills Detail

def Skilldetail(request,user=None,pk=None):

    qs=TechnicalSkills.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/skill_detail.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Skills

def UpdateTechnicalSkill(request,user=None,pk=None):

    instance=TechnicalSkills.objects.get(user=request.user,pk=pk)
    form=TechnicalSkillCreateForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Technical Skills")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_skill.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)

# Delete Skills

def DeleteTechnicalSkill(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=TechnicalSkills.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Technical Skills")
    return HttpResponseRedirect("/students/profile")

# Create Educational Informations

def CreateEducationalInfo(request):

    form=EducationalInfoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Added Educational Informations")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_edu.html"
    context={"form":form}

    return render(request,template_name,context)

# Educational Informations List

def EducationalInfoList(request):

    qs=Education.objects.filter(user=request.user)
    template_name="cv_portfolio/edu_info_list.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Educational Informations Detail

def EducationalInfoDetail(request,user=None,pk=None):

    qs=Education.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/edu_info_detail.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Educational Informations

def UpdateEducationalInfo(request,user=None,pk=None):

    instance=Education.objects.get(user=request.user,pk=pk)
    form=EducationalInfoForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Educational Informations")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_edu.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)

# Delete Educational Informations

def DeleteEducationalInfo(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=Education.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Educational Informations")
    return HttpResponseRedirect("/students/profile")

# Create Work History

def CreateWorkHistory(request):

    form=WorkHistoryForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Added Work History")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_work.html"
    context={"form":form}

    return render(request,template_name,context)

# Work History Detail

def WorkHistoryList(request):

    qs=WorkHistory.objects.filter(user=request.user)
    template_name="cv_portfolio/list_work.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Detail Work History

def DetailHistoryList(request,user=None,pk=None):

    qs=WorkHistory.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/detail_work.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Work Hiwstory

def UpdateWorkHistory(request,user=None,pk=None):

    instance=WorkHistory.objects.get(user=request.user,pk=pk)
    form=WorkHistoryForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Work History")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_work.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)

# Delete Work History

def DeleteWorkHistory(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=WorkHistory.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Work History")
    return HttpResponseRedirect("/students/profile")


# Upload Resume

def UploadResume(request):

    user_exists=UploadCV.objects.filter(user=request.user).exists()
    form=ResumeUploadForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        if not user_exists:
            instance.save()
            messages.success(request, "Successfully Upload Your Resume")
            return HttpResponseRedirect("/students/profile")
        else:
            return render(request,"cv_portfolio/exists.html",{})

    template_name="cv_portfolio/upload_resume.html"
    context={"form":form}

    return render(request,template_name,context)

# Update Resume

def UpdateResume(request):

    instance=UploadCV.objects.get(user=request.user)
    form=ResumeUploadForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Your Resume")
        return HttpResponseRedirect("/students/profile")


    template_name="cv_portfolio/update_resume.html"
    context={"form":form}

    return render(request,template_name,context)


# Create Portfolio

def PortfolioView(request):

    form=PortfolioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Created Protfolio.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_portfolio.html"
    context={"form":form}

    return render(request,template_name,context)


# Portfolio Description

def PortfolioDetail(request,pk=None):

    qs=Portfolio.objects.get(pk=pk)
    user_=Profile.objects.get(user=qs.user)
    template_name="cv_portfolio/portfolio_detail.html"
    context={"qs":qs,"user_":user_}

    return render(request,template_name,context)

# Portfolio List

def PortfolioList(request):

    qs=Portfolio.objects.filter(user=request.user)
    template_name="cv_portfolio/portfolio_list.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Portfolio Detail For User

def PortfolioDetailforUser(request,user=None,pk=None):

    qs=Portfolio.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/portfolio_detail_user.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Portfolio

def UpdatePortfolio(request,user=None,pk=None):

    instance=Portfolio.objects.get(user=request.user,pk=pk)
    form=PortfolioForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Your Portfolio")
        return HttpResponseRedirect("/students/profile")


    template_name="cv_portfolio/update_portfolio.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)


# Delete Portfolio

def DeletePortfolio(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=Portfolio.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Portfolio")
    return HttpResponseRedirect("/students/profile")

# Create Service

def ServiceCreationView(request):

    form=ServiceCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Added Service Informations.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_service.html"
    context={"form":form}

    return render(request,template_name,context)

# Service Information List

def ServiceInfoList(request):

    qs=Service.objects.filter(user=request.user)
    template_name="cv_portfolio/service_info_list.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Service Informations Detail

def ServiceInfoDetail(request,user=None,pk=None):

    qs=Service.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/service_info_detail.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Service Informations

def UpdateServiceInfo(request,user=None,pk=None):

    instance=Service.objects.get(user=request.user,pk=pk)
    form=ServiceCreationForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Your Service Informations")
        return HttpResponseRedirect("/students/profile")


    template_name="cv_portfolio/update_service_info.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)

# Delete Service

def DeleteService(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=Service.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Service Informations.")
    return HttpResponseRedirect("/students/profile")

# Create Success Informations

def CreationSuccessInfo(request):

    info_exists=Succeess.objects.filter(user=request.user).exists()
    form=SuccessCreationForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        if not info_exists:
            instance.save()
            messages.success(request, "Successfully Added Success Informations.")
            return HttpResponseRedirect("/students/profile")
        else:
            return render(request,"cv_portfolio/exists.html",{})


    template_name="cv_portfolio/create_success_info.html"
    context={"form":form}

    return render(request,template_name,context)

# Update Success Informations

def UpdateSuccessInfo(request):

    instance=Succeess.objects.get(user=request.user)
    form=SuccessCreationForm(request.POST or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Success Informations.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_success_info.html"
    context={"form":form}

    return render(request,template_name,context)

# Create Working Process

def CreationWorkingProcess(request):


    form=WorkingProcessCreationForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Added Working Proccess.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_working_process.html"
    context={"form":form}

    return render(request,template_name,context)

# Working Process List

def WorkingProcessList(request):

    qs=WorkingProcess.objects.filter(user=request.user)
    template_name="cv_portfolio/working_process_list.html"
    context={"qs":qs}
    return render(request,template_name,context)

# Working Process Detail

def WorkingProcessDetail(request,user=None,pk=None):

    qs=WorkingProcess.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/working_process_detail.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Working Process

def UpdateWorkingProcess(request,user=None,pk=None):

    instance=WorkingProcess.objects.get(user=request.user,pk=pk)
    form=WorkingProcessCreationForm(request.POST or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Working Proccess.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_working_process.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)

# Delete Working Process

def DeleteWorkingProcess(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=WorkingProcess.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Working Process.")
    return HttpResponseRedirect("/students/profile")


# Create Clients

def CreateClients(request):

    form=ClientsCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Created Your Clients.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/create_clients.html"
    context={"form":form}

    return render(request,template_name,context)

# Clients List

def ClientList(request):

    qs=Clients.objects.filter(user=request.user)
    template_name="cv_portfolio/clients_list.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Clients Detail

def ClientDetail(request,user=None,pk=None):

    qs=Clients.objects.get(user=request.user,pk=pk)
    template_name="cv_portfolio/clients_detail.html"
    context={"qs":qs}

    return render(request,template_name,context)

# Update Clients

def UpdateClients(request,user=None,pk=None):

    instance=Clients.objects.get(user=request.user,pk=pk)
    form=ClientsCreationForm(request.POST or None, request.FILES or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, "Successfully Updated Your Clients.")
        return HttpResponseRedirect("/students/profile")

    template_name="cv_portfolio/update_clients.html"
    context={"form":form,"instance":instance}

    return render(request,template_name,context)

# Delete Clients


def DeleteClients(request,user=None,pk=None):

    if not request.user.is_authenticated:
        raise Http404

    instance=Clients.objects.get(user=request.user,pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Clients")
    return HttpResponseRedirect("/students/profile")
