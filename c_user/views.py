from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.html import json_script
from .forms import RegisterForm, LoginForm
from .models import Company, C_user


def login_temp_view(request):
    template = "./c_user/login.html"
    context = {"err": "", "companies": Company.objects.all()}
    print("companies", context)
    if request.method == "POST":
        print("its a post", request.POST)
        post_data = LoginForm(request.POST)
        if post_data.is_valid():
            cred_ = {
                "username": post_data.cleaned_data["username"],
                "password": post_data.cleaned_data["password"],
            }
            # check the user credentials
            the_user = authenticate(request, **cred_)
            # when there is no user.
            if not the_user:
                context["err"] = "Invalid username or password!"
                return render(request, template, {**context})
            # login the user
            login(request, the_user)
            return redirect("stock:dashboard")
        # invalid post data
        context["err"] = post_data.errors
        return render(request, template, {**context})
    # get request
    print("its a get request.")
    return render(request, template, context)


def register_view(request):
    context = {"companies": Company.objects.all()}
    template = "./c_user/register.html"
    if not request.method == "POST":
        return render(request, template)
    _form = RegisterForm(request.POST)

    if _form.is_valid():
        # print("form data ", _form.cleaned_data)
        # validation.
        valid_field, err_reason = validate_register_fields(_form.cleaned_data)
        if not valid_field:
            print("not valid field ", err_reason)
            return render(
                request,
                template,
                {**context, "register_status": err_reason},
            )
        try:
            new_company = Company.objects.create(title=_form.cleaned_data["company"])
            u = C_user.objects.create(
                username=_form.cleaned_data["username"],
                email=_form.cleaned_data["email"],
                company=new_company,
            )
            u.set_password(_form.cleaned_data["password"])
            u.save()
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


def validate_register_fields(fields):
    state = True
    reason = None
    if Company.objects.filter(title=fields["company"]).exists():
        return False, "Company name already exists."
    if fields["password"] != fields["re_password"]:
        return False, "Passwords do no match!"
    return state, reason
