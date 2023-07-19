from django.contrib import admin
from .models import student
from .models import Login
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['studentname','studentid','gender','status']
admin.site.register(student , studentAdmin)
admin.site.site_header = 'Edit data student'
admin.site.site_title = 'Edit data student'
admin.site.register(Login)
