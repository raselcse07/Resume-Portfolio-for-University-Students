from django.conf.urls import url
from . import views

app_name="Notifications"

urlpatterns = [
    url(r'^notification/(?P<slug>[-\w]+)/$', views.NotificationsView,name="notification"),

]
