from django import forms
from .models import C_user
from .models import Company

class RegisterForm(forms.Form):
    company_type =forms.CharField(max_length=255) 
    company = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    password= forms.CharField(max_length=255)
    re_password =  forms.CharField(max_length=255)
    email = forms.EmailField()


class LoginForm(RegisterForm):
    company = forms.IntegerField()
    email = forms.CharField(required=False)
    company_type = forms.CharField(required=False)
    re_password = forms.CharField(required=False)

