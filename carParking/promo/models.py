from django.db import models
from django.conf import settings


class Promo(models.Model):
    promo = models.TextField('Промокод')
    prize = models.IntegerField('Приз')
    isActive = models.BooleanField('Действителен', default=True)

    def __str__(self):
        return self.promo

    def get_absolute_url(self):
        return f'/promo/{self.id}'

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'