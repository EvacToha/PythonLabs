from django.db import models


class Faq(models.Model):
    title = models.CharField('Название вопроса', max_length=100)
    anons = models.CharField('Анонс вопроса', max_length=300)
    full_text = models.TextField('Текст вопроса')
    answer_text = models.TextField('Ответ на вопрос', default='')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/faq/{self.id}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


