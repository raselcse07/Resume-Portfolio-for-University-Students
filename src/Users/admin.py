from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser,Profile,ActivationProfile
from .forms import UserCreationForm,UserChangeForm



class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin','is_staff',)}),
        ('Access', {'fields': ('is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username','email',)
    ordering = ('username','email',)
    filter_horizontal = ()


class ActivationProfileModelAdmin(admin.ModelAdmin):

    list_display=["user","key","expired"]
    list_display_links=["user"]
    list_filter=["user"]

    class Meta:

        model=ActivationProfile

class ProfileModelAdmin(admin.ModelAdmin):

    list_display=["reg_number","user","dept_name","academic_year","CGPA"]
    list_display_links=["user"]
    list_filter=["user","dept_name","reg_number","academic_year","CGPA"]

    class Meta:

        model=Profile

admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile,ProfileModelAdmin)
admin.site.register(ActivationProfile,ActivationProfileModelAdmin)
admin.site.unregister(Group)
