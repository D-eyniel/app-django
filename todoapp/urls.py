from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import redirect
from todoapp import views

urlpatterns = [
    path("register/", views.register_view, name="register"),  # Registration page
    path("login/", views.login_view, name="login"),           # Login page
    path("dashboard/", views.dashboard, name="dashboard"),   # Dashboard page
    path('', lambda request: redirect('login')),  # Redirect root URL to login page
     path("forgot-password/", views.forgot_password, name="forgot_password"),

]
