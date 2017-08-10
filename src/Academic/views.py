from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,HttpResponse
from .models import Department
from Users.models import Profile
from Users.forms import ProfileUpdateForm,ProfileCreateForm
from cv_portfolio.models import(TechnicalSkills,
                                Education,
                                WorkHistory,
                                Portfolio,
                                AdditionalInfo,
                                Clients,
                                Service,
                                Succeess,
                                WorkingProcess)




def DepartmentView(request):

    dept_list_qs=Department.objects.all()

    template_name="Academic/department_list.html"
    context={

        "dept_list_qs":dept_list_qs,

    }

    return render(request,template_name,context)


def DepartmentDetail(request,dept_name_short=None):

    dept_name=Department.objects.filter(dept_name_short=dept_name_short)
    qs=Profile.objects.filter(dept_name=dept_name)

    template_name="Academic/department_detail.html"
    context={

        "qs":qs,
    }

    return render(request,template_name,context)


def StudentList(request,dept_name=None,dept_session=None):

    dept_name   =Department.objects.get(dept_name_short=dept_name)

    if dept_name:

        qs=Profile.objects.filter(dept_name=dept_name,academic_year=dept_session)

        paginator = Paginator(qs, 25) # Show 25 student_list per page

        page = request.GET.get('page')
        try:
            student_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            student_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            student_list = paginator.page(paginator.num_pages)

    template_name="Academic/profile_list.html"

    context={
            "qs":qs,
            "dept_name":dept_name,
            "student_list":student_list
    }

    return render(request,template_name,context)


def StudentDetail(request,dept_name=None,dept_session=None,reg_number=None):

    try:

        dept_name   =Department.objects.get(dept_name_short=dept_name)

        if dept_name:

            qs=Profile.objects.get(dept_name=dept_name,academic_year=dept_session,reg_number=reg_number)
            add_info=AdditionalInfo.objects.filter(user=qs.user)
            skill_=TechnicalSkills.objects.filter(user=qs.user)
            education=Education.objects.filter(user=qs.user)
            work=WorkHistory.objects.filter(user=qs.user)
            port_folio=Portfolio.objects.filter(user=qs.user)
            clients=Clients.objects.filter(user=qs.user)
            service=Service.objects.filter(user=qs.user)
            success=Succeess.objects.filter(user=qs.user)
            work_process=WorkingProcess.objects.filter(user=qs.user)
            x=work_process.count() // 2

        template_name="Academic/profile_detail.html"
        context={
                    "qs":qs,
                    "dept_name":dept_name,
                    "skill_":skill_,
                    "education":education,
                    "work":work,
                    "port_folio":port_folio,
                    "add_info":add_info,
                    "clients":clients,
                    "service":service,
                    "success":success,
                    "work_process1":work_process[:x],
                    "work_process2":work_process[x:]

                }

        return render(request,template_name,context)

    except:

        return render(request,"Academic/profile404.html",{})


def ProfileUpdate(request,dept_name=None,dept_session=None,reg_number=None):

    dept_name   =Department.objects.get(dept_name_short=dept_name)

    if dept_name:

        instance=Profile.objects.get(dept_name=dept_name,academic_year=dept_session,reg_number=reg_number)

    form =ProfileUpdateForm(request.POST or None,instance=instance)

    if form.is_valid():

        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated Your Informations")
        return HttpResponseRedirect("/students/profile")

    template_name="Academic/profile_update.html"
    context={"instance":instance,"form":form}

    return render(request,template_name,context)


def ProfileCreate(request):

    user_exists=Profile.objects.filter(user=request.user).exists()
    form=ProfileCreateForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        if not user_exists:
            instance.save()
            messages.success(request, "Successfully Created Your Profile")
            return HttpResponseRedirect("/students/profile")
        else:
            return HttpResponse("Profile Already Exists")

    template_name="Academic/profile_create.html"
    context={
        "form":form
    }

    return render(request,template_name,context)
