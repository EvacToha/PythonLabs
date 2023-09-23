import requests

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from news.models import Articles


def index(request):
    earliest_news = Articles.objects.earliest('date')
    data = {
        'news': earliest_news
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def openings(request):
    return render(request, 'main/openings.html')


@login_required
def profile(request):
    user = request.user
    profile_user = Profile.objects.get(user_id=user.id)
    data = {
        'user': user,
        'profile': profile_user
    }
    return render(request, 'main/profile.html', data)


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


def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')
