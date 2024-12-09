from django import forms
from .models import DemoSession

class DemoSession(forms.ModelForm):
    class Meta:
        model = DemoSession
        fields = ['full_name', 'email', 'phone_number', 'preferred_day', 'preferred_time']
