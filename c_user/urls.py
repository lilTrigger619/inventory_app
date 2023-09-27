from .views import login_temp_view, register_view
from django.urls import path
from django.contrib.auth.views import LoginView

app_name = "auth"

urlpatterns = [
        path("llogin/", LoginView.as_view(template_name="c_user/login.html")),
        path("login/", login_temp_view, name="login"),
        path("register/", register_view, name="register"),
]

