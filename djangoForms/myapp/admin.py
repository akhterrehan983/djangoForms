from django.contrib import admin

from .models import userForm,incidentReport

class userFormAdmin(admin.ModelAdmin):
    list_display = ['id']

class incidentReportAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(userForm,userFormAdmin)
admin.site.register(incidentReport,incidentReportAdmin)

