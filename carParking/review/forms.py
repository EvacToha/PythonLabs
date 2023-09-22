from .models import Review
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput


class ReviewsForm(ModelForm):
    class Meta:
        model = Review
        fields = ['full_text', 'grade', 'date']

        widgets = {
            "grade": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка от 1 до 5',
                'min': 1,
                'max': 5
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата отзыва',
                'type': 'date'
            })
        }
