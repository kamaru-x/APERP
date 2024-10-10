from django.contrib import admin
from Core.models import Department, Lead, FollowUp, Booking

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','id']

admin.site.register(Department, DepartmentAdmin)

class LeadAdmin(admin.ModelAdmin):
    list_display = ['name','location','type','district','sub_district']

admin.site.register(Lead, LeadAdmin)

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ['lead','date','title']

admin.site.register(FollowUp, FollowUpAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['lead','date','status','students','teachers','visit_date']

admin.site.register(Booking, BookingAdmin)