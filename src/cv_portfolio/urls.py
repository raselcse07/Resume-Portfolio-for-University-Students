from django.conf.urls import url
from . import views

app_name="cv_portfolio"

urlpatterns = [

    # Create Informations

    url(r'^aditionalinfo/create/$', views.CreateAdditionalInfo,name="create_aditionalinfo"),
    url(r'^resume/upload/$', views.UploadResume,name="upload_resume"),
    url(r'^portfolio/create/$', views.PortfolioView,name="create_portfolio"),
    url(r'^skills/create/$', views.CreateTechnicalSkill,name="create_skill"),
    url(r'^education/create/$', views.CreateEducationalInfo,name="create_edu"),
    url(r'^work/create/$', views.CreateWorkHistory,name="create_work"),
    url(r'^service/create/$', views.ServiceCreationView,name="service"),
    url(r'^success/create/$', views.CreationSuccessInfo,name="success"),
    url(r'^working_process/create/$', views.CreationWorkingProcess,name="working_process"),
    url(r'^clients/create/$', views.CreateClients,name="create_clients"),

    # List and Detail

    url(r'^skills/list/$', views.SkillList,name="skill_list"),
    url(r'^(?P<user>[-\w]+)/skills/(?P<pk>[-\d]+)/detail/$', views.Skilldetail,name="skill_detail"),

    url(r'^portfolio/list/$', views.PortfolioList,name="portfolio_list"),
    url(r'^portfolio/(?P<pk>[-\d]+)/detail/$', views.PortfolioDetail,name="portfolio_detail"),
    url(r'^(?P<user>[-\w]+)/portfolio/(?P<pk>[-\d]+)/detail/$', views.PortfolioDetailforUser,name="portfolio_detail_user"),

    url(r'^education/list/$', views.EducationalInfoList,name="edu_list"),
    url(r'^(?P<user>[-\w]+)/education/(?P<pk>[-\d]+)/detail/$', views.EducationalInfoDetail,name="edu_detail"),

    url(r'^work/list/$', views.WorkHistoryList,name="work_list"),
    url(r'^(?P<user>[-\w]+)/work/(?P<pk>[-\d]+)/detail/$', views.DetailHistoryList,name="work_detail"),

    url(r'^service/list/$', views.ServiceInfoList,name="service_list"),
    url(r'^(?P<user>[-\w]+)/service/(?P<pk>[-\d]+)/detail/$', views.ServiceInfoDetail,name="service_detail"),

    url(r'^working_process/list/$', views.WorkingProcessList,name="working_process_list"),
    url(r'^(?P<user>[-\w]+)/working_process/(?P<pk>[-\d]+)/detail/$', views.WorkingProcessDetail,name="working_process_detail"),

    url(r'^clients/list/$', views.ClientList,name="clients_list"),
    url(r'^(?P<user>[-\w]+)/clients/(?P<pk>[-\d]+)/detail/$', views.ClientDetail,name="clients_detail"),




    # Update Informations

    url(r'^aditionalinfo/edit/$', views.UpdateAdditionalInfo,name="update_aditionalinfo"),
    url(r'^resume/edit/$', views.UpdateResume,name="update_resume"),
    url(r'^success/edit/$', views.UpdateSuccessInfo,name="update_success"),
    url(r'^(?P<user>[-\w]+)/skills/(?P<pk>[-\d]+)/edit/$', views.UpdateTechnicalSkill,name="update_skill"),
    url(r'^(?P<user>[-\w]+)/education/(?P<pk>[-\d]+)/edit/$', views.UpdateEducationalInfo,name="update_edu"),
    url(r'^(?P<user>[-\w]+)/portfolio/(?P<pk>[-\d]+)/edit/$', views.UpdatePortfolio,name="update_portfolio"),
    url(r'^(?P<user>[-\w]+)/work/(?P<pk>[-\d]+)/edit/$', views.UpdateWorkHistory,name="update_work"),
    url(r'^(?P<user>[-\w]+)/service/(?P<pk>[-\d]+)/edit/$', views.UpdateServiceInfo,name="update_service_info"),
    url(r'^(?P<user>[-\w]+)/working_process/(?P<pk>[-\d]+)/edit/$', views.UpdateWorkingProcess,name="update_working_process"),
    url(r'^(?P<user>[-\w]+)/clients/(?P<pk>[-\d]+)/edit/$', views.UpdateClients,name="update_clients"),


    # Delete Informations

    url(r'^(?P<user>[-\w]+)/skills/(?P<pk>[-\d]+)/delete/$', views.DeleteTechnicalSkill,name="delete_skill"),
    url(r'^(?P<user>[-\w]+)/education/(?P<pk>[-\d]+)/delete/$', views.DeleteEducationalInfo,name="delete_edu"),
    url(r'^(?P<user>[-\w]+)/portfolio/(?P<pk>[-\d]+)/delete/$', views.DeletePortfolio,name="delete_portfolio"),
    url(r'^(?P<user>[-\w]+)/work/(?P<pk>[-\d]+)/delete/$', views.DeleteWorkHistory,name="delete_work"),
    url(r'^(?P<user>[-\w]+)/service/(?P<pk>[-\d]+)/delete/$', views.DeleteService,name="delete_service"),
    url(r'^(?P<user>[-\w]+)/working_process/(?P<pk>[-\d]+)/delete/$', views.DeleteWorkingProcess,name="delete_working_process"),
    url(r'^(?P<user>[-\w]+)/clients/(?P<pk>[-\d]+)/delete/$', views.DeleteClients,name="delete_clients"),



]
