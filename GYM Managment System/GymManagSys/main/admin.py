from django.contrib import admin
from .models import LoginRecord
from django.contrib import admin
from .models import DemoSession

@admin.register(DemoSession)
class DemoSessionForm(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'preferred_day', 'preferred_time')

@admin.register(LoginRecord)
class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time')
