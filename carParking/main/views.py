import requests


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import UserCreateForm
from service.models import Client

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
    form = UserCreateForm()
    data = {
        'form': form
    }
    return render(request, 'registration/register.html', data)


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = 'login/'

    template_name = 'registration/register.html'
    def form_valid(self, form) -> HttpResponse:
        form.save()

        Client.objects.create(first_name=form.cleaned_data['first_name'],
                              last_name=form.cleaned_data['last_name'],
                              date_of_birth=form.cleaned_data['date_of_birth'],
                              email=form.cleaned_data['email'],
                              phone_number=form.cleaned_data['phone_number'],
                              money=0).save()

        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form) -> HttpResponse:
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = '/registration/login.html'

    quote = requests.get('https://favqs.com/api/qotd').json()

    def get(self, request):
        return render(request, 'registration/login.html',
                      context={'form': self.form_class(), 'quote': self.quote['quote']['body']})

    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(FormView):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')