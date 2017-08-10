from django.shortcuts import render
from .models import AdminMessage




def NotificationsView(request,slug=None):

    qs=AdminMessage.objects.filter(slug=slug)

    template_name="Notifications/notification.html"
    context={"qs":qs}

    return render(request,template_name,context)
