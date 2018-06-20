from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserForm

# Create your views here.

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            create_user = form.save()
            create_user.set_password(create_user.password)
            create_user.save()
            return HttpResponse("User created with success!")
    else:
        form = UserForm()
    return render(request, 'accounts/create_user.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        verify_user = authenticate(username=username, password=password)

        if verify_user:
            login(request, verify_user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, "Username or Password is invalid!")

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('accounts:change_password')
        else:
            messages.error(request, "Something is wrong! Try again...")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
