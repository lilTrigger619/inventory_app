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

    def validate(self):
        print("validation took place!")
        # if company type is new then
        # the user must change the company name if it already exist
        if self.company_type == "new":
            try:
                Company.objects.get(title=self.company)
                raise forms.ValidationError("company name alread exists!")
            except:
                pass
            try:
                C_user.objects.get(title=self.company)
                raise forms.ValidationError("company name alread exists!")
            except:
                pass
        if self.password != self.re_password:
            raise forms.ValidationError("passwords do not match")
