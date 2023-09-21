from .models import Auto
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput


class AutosForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['brand', 'model', 'image']

        widgets = {
            "brand": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка',
                'enctype': 'multipart/form-data'
            })
        }
