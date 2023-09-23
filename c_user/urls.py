from .views import login_view, register_view
from django.urls import path

app_name = "auth"

urlpatterns = [
        path("login/", login_view, name="login"),
        path("register/", register_view, name="register"),
]

