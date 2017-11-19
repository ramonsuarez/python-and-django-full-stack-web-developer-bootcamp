from django import forms
from AppTwo.models import User


class NewUserForm(forms.ModelForm):
    # If you want validators add fields here
    class Meta():
        model = User
        fields = '__all__'
