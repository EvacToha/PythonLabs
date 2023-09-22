from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField('Имя пользователя', max_length=100)
    full_text = models.TextField('Отзыв')
    grade = models.IntegerField('Оценка')
    dis_grade = models.IntegerField('Оценка в минус',default=0)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/review/{self.id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


