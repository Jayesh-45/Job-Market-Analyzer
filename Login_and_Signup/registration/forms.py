from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput}

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
