from .models import Place
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput, NumberInput


class PlacesForm(ModelForm):
    class Meta:
        model = Place
        fields = ['number', 'price']

        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })
        }
