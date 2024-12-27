from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

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

# Forgot password view
def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = User.objects.get(username=username)

            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been updated successfully!')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match.')

        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'password_reset.html')

# Dashboard view
def dashboard(request):
    return render(request, "dashboard.html")
