from django.db import models

from django.conf import settings


class Auto(models.Model):
    brand = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=250)
    image = models.ImageField('Картинка', upload_to='images/')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.brand + ' ' + self.model

    def get_absolute_url(self):
        return f'/cars/{self.id}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'