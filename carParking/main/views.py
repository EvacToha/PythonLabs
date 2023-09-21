import requests


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Profile


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
