from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)