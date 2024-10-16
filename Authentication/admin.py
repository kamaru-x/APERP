from django.contrib import admin
from Authentication.models import Source, Group, User

# Register your models here.

class SourceAdmin(admin.ModelAdmin):
    list_display = ['name','date']

admin.site.register(Source, SourceAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','source','date']

admin.site.register(Group, GroupAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email']

admin.site.register(User, UserAdmin)