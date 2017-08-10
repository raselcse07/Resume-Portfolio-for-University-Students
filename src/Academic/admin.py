from django.contrib import admin
from .models import Department


class DepartmentModelAdmin(admin.ModelAdmin):

    list_display=["dept_name","dept_name_short"]
    list_display_links=["dept_name","dept_name_short"]
    search_fields=["dept_name","dept_name_short"]
    list_filter=["dept_name","dept_name_short"]

    class Meta:

        model=Department


# class SessionAdminModel(admin.ModelAdmin):
#
#     list_display=["dept_session","dept_name"]
#     list_filter=["dept_name","dept_session"]
#     search_fields=["dept_name","dept_session"]
#     list_display_links=["dept_name","dept_session"]
#
#     class Meta:
#
#         model=Session

admin.site.register(Department,DepartmentModelAdmin)
# admin.site.register(Session,SessionAdminModel)
