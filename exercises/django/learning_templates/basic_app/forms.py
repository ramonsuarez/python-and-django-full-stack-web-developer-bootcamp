from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

class Meta():
    model = UserProfileInfoForm
    fields = ('portfolio_site', 'profile_pic')
