from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class Buyer(AbstractUser):
    first_name = models.CharField(max_length=200,
                                  help_text='Введите имя')
    last_name = models.CharField(max_length=200,
                                 help_text='Введите фамилию')
    date_of_birth = models.DateField()
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(max_length=50,
                                    help_text='Введите номер')
    money = models.FloatField('Деньги')

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'money']