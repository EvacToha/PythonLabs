from django.db import models
from django.conf import settings

from auto.models import Auto


class Place(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.DO_NOTHING, null=True, blank=True)
    number = models.IntegerField('Номер парковки')
    price = models.FloatField('Цена', default=0)

    def __str__(self):
        return 'Place {}'.format(self.number)
