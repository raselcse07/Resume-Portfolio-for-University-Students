from django.contrib import admin
from .models import AdminMessage



class AdminMessageModelAdmin(admin.ModelAdmin):

    list_display=["title","publish","timestamp","updated"]
    list_display_links=["title"]
    
    class Meta:

        model = AdminMessage

admin.site.register(AdminMessage,AdminMessageModelAdmin)
