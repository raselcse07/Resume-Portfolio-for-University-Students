from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name="Users"

urlpatterns = [

    url(r'^register/$',views.Register,name="register"),
    url(r'^login/$',views.UserLogin,name="login"),
    url(r'^logout/$',views.User_Logout,name="logout"),
    url(r'^profile/$',views.ProfileView,name="profile"),
    url(r'^activate/(?P<code>[a-z0-9].*)/$',views.ActivateProfile,name="activate"),

    # Password Reset

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views. password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # Password Change

    url(r'^password_change/$', auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),

]
