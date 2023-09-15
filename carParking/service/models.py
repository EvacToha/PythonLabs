from django.db import models
from django.urls import reverse

class Client(models.Model):
    first_name = models.CharField(max_length=200,
                                  help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                 help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')
    money = models.FloatField()

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)