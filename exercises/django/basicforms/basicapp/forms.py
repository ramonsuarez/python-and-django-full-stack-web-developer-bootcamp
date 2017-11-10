from django import forms

class FormName(forms.Form):
    name = form.CharField()
    email = form.EmailField()
    text = form.CharField(widget=forms.Text)
