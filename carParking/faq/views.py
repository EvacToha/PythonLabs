from django.shortcuts import render, redirect
from .models import Faq
from django.views.generic import DetailView


def faq_home(request):
    faq = Faq.objects.all()

    data = {
        'faq': faq
    }
    return render(request, 'faq/faq_home.html', data)


class FaqDetailView(DetailView):
    model = Faq
    template_name = 'faq/details_view.html'
    context_object_name = 'faq'