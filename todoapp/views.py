from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Register view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("dashboard")  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

# Dashboard view
def dashboard(request):
    return render(request, "dashboard.html")
