from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def review_home(request):
    reviews = Review.objects.all()

    data = {
        'reviews': reviews
    }
    return render(request, 'review/review_home.html', data)


def create_review(request):
    error = ''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.username = request.user.username
            new_review.dis_grade = 5 - new_review.grade
            new_review.save()
            return redirect('review_home')
        else:
            error = 'Форма заполнена некорректно'
    form = ReviewsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'review/create_review.html', data)
