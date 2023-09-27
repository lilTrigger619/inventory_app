from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.utils.html import json_script
from .forms import RegisterForm
from .models import Company, C_user


def login_temp_view(request):
    template = "./c_user/login.html"
    if not request.method == "POST":
        print("redirection made")
        return redirect("/auth/llogin")
    return render(request, template)


def register_view(request):
    context = {"companies": Company.objects.all()}
    template = "./c_user/register.html"
    if not request.method == "POST":
        return render(request, template)
    _form = RegisterForm(request.POST)
    _form.validate()
    if _form.is_valid():
        print("form data ", _form.cleaned_data)
        try:
            new_company = Company.objects.create(title=_form.cleaned_data["company"])
            C_user.objects.create(
                username=_form.cleaned_data["username"],
                email=_form.cleaned_data["email"],
                company=new_company,
            )
        except Exception as e:
            print("error while registering ", e)
            return render(
                request,
                template,
                {**context, "register_status": "An unknown error while registering"},
            )

        return render(request, template, {**context, "register_status": 201})
    print("form errors ", _form.errors)
    return render(request, template, {**context, "register_status": _form.errors})
