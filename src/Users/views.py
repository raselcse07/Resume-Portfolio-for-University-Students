from datetime import date
from django.shortcuts import render
from django.contrib import messages
from .forms import UserCreationForm,UserLoginForm
from django.contrib.auth import login,get_user_model,logout
from django.http import HttpResponseRedirect,Http404
from .models import ActivationProfile,Profile
from Notifications.models import AdminMessage
from cv_portfolio.models import TechnicalSkills,WorkHistory,Portfolio,Service


User=get_user_model()



def Register(request,*args,**kwargs):

    form=UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"Successfully registered.Please Check your email to activate your Account")
        return HttpResponseRedirect("/students/login")

    template_name="Users/register.html"
    context={
                "form":form

            }

    return render(request,template_name,context)


def UserLogin(request,*args,**kwargs):

    form=UserLoginForm(request.POST or None)

    if form.is_valid():

        user_obj =form.cleaned_data.get('user_obj')
        login(request,user_obj)
        return HttpResponseRedirect("/students/profile")

    template_name="Users/login.html"
    context={
                "form":form

            }
    return render(request,template_name,context)


def User_Logout(request):

    logout(request)
    messages.success(request,"Successfully Logged out.")
    return HttpResponseRedirect("/students/login")

# Activate Profile.Need to activate profile for login.

def ActivateProfile(request,code=None,*args,**kwars):

    if code:

        act_profile_qs=ActivationProfile.objects.filter(key=code)

        if act_profile_qs.exists() and act_profile_qs.count() == 1:

            act_obj=act_profile_qs.first()
            if not act_obj.expired:

                user_obj=act_obj.user
                user_obj.is_active=True
                user_obj.save()
                act_obj.expired=True
                act_obj.save()
                messages.success(request,"Successfully activated your accounts.Now you can login to our site")
                return HttpResponseRedirect("/students/login")

    raise Http404

# User Admin Panel.

def ProfileView(request):

    try:

        if request.user.is_authenticated:


            qs=Profile.objects.get(user=request.user)
            skill_=TechnicalSkills.objects.filter(user=qs.user)
            work_history=WorkHistory.objects.filter(user=qs.user).count()
            port_folio=Portfolio.objects.filter(user=qs.user).count()
            total_skill=skill_.count()
            today = date.today()
            notifications=AdminMessage.objects.filter(publish__year=today.year, publish__month=today.month, publish__day=today.day)
            message_=AdminMessage.objects.all()[:10]
            service_info=Service.objects.filter(user=qs.user).count()
            template_name="Users/profile.html"
            context={
                        "qs":qs,
                        "total_skill":total_skill,
                        "work_history":work_history,
                        "port_folio":port_folio,
                        "notifications":notifications,
                        "message_":message_,
                        "service_info":service_info
                    }

            return render(request,template_name,context)
        else:
            return HttpResponseRedirect("/students/login")

    except:

        return render(request,"Users/profile404.html",{})
