from django.conf.urls import url
from . import views
from cv_portfolio.views import PreviewCV,PortfolioView

app_name="Academic"

urlpatterns = [
    url(r'^$', views.DepartmentView,name="dept_list"),
    url(r'^(?P<dept_name_short>[-\w]+)/list/$', views.DepartmentDetail,name="dept_detail"),
    url(r'^(?P<dept_name>[-\w]+)/list/(?P<dept_session>[\w-]+)/$', views.StudentList,name="profile_list"),
    url(r'^(?P<dept_name>[-\w]+)/list/(?P<dept_session>[\w-]+)/(?P<reg_number>[\w-]+)/$', views.StudentDetail,name="detail"),
    url(r'^(?P<dept_name>[-\w]+)/list/(?P<dept_session>[\w-]+)/(?P<reg_number>[\w-]+)/edit/$', views.ProfileUpdate,name="update"),
    url(r'^(?P<dept_name>[-\w]+)/list/(?P<dept_session>[\w-]+)/(?P<reg_number>[\w-]+)/cv/$',PreviewCV,name="cv"),
    # url(r'^(?P<dept_name>[-\w]+)/list/(?P<dept_session>[\w-]+)/(?P<reg_number>[\w-]+)/portfolio/$',PortfolioView,name="portfolio"),
    url(r'^profile/create/$', views.ProfileCreate,name="create"),


]
