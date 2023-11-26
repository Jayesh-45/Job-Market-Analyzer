# forms.py
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password=forms.CharField(max_length=30)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)