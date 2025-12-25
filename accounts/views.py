from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
