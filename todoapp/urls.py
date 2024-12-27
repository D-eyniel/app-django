from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="home"),           # Root path ("/") mapped to login_view
    path("login/", views.login_view, name="login"),    # Login page
    path("register/", views.register_view, name="register"),  # Registration page
    path("dashboard/", views.dashboard, name="dashboard"),   # Dashboard page
]
