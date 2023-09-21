from django import forms
from django.contrib.auth.models import User
from django.forms import DateTimeInput, TextInput


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Пароль', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Повторите пароль', 'type': 'password'}))
    date_of_birth = forms.CharField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата рождения', 'type': 'date'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Телефон'}))

    class Meta:
        model = User

        fields = ['username', 'email', 'date_of_birth', 'phone_number', 'password', 'password2']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }),
            "email": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
                'type': 'email'
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
