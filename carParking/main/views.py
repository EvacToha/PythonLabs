import requests

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from .models import Profile
from django.contrib.auth import authenticate, login

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_profile = Profile(date_of_birth=user_form.cleaned_data['date_of_birth'], phone_number=user_form.cleaned_data['phone_number'])
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile.user_id = User.objects.get(email=new_user.email).id
            new_profile.save()

            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Некорректные данные')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
