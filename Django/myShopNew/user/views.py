from django.shortcuts import render, redirect

# For Login And LogOut
from .forms import CreateUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user.models import *


# Create your views here.

@login_required(login_url='/login')  # Check login
def user(request):
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile': profile}
    return render(request, 'user_profile.html', context)


def login_form(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is not correct!')

        return render(request, 'login_form.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(
                    request, username=username, password=password)
                login(request, user)
                # Create data in profile table for user
                current_user = request.user
                data = UserProfile()
                data.user_id = current_user.id
                data.save()
                messages.success(
                    request, 'Account was created for ' + username)
                return redirect('index')
            else:
                messages.warning(request, form.errors)
                return redirect('signup')

        context = {'form': form}
        return render(request, 'signup_form.html', context)


@login_required(login_url='login')
def logout_func(request):
    auth_logout(request)
    return redirect('index')
