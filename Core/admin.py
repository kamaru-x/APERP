from django.contrib import admin
from Core.models import Department, Lead

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','id']

admin.site.register(Department, DepartmentAdmin)

class LeadAdmin(admin.ModelAdmin):
    list_display = ['name','location','type','district','sub_district']

admin.site.register(Lead, LeadAdmin)