from django import forms
from django.forms import ModelForm
from .models import AccountInfo



class RegisterForm(ModelForm):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=PasswordInput)

    class Meta:
        model = AccountInfo
        fields = ["username", "password"]