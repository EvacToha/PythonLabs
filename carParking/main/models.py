from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField('Дата рождения')
    phone_number = models.CharField('Телефон', max_length=19)
    money = models.FloatField('Деньги', default=0)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)