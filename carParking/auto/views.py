from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Auto
from .forms import AutosForm
from django.views.generic import DetailView, UpdateView, DeleteView


@login_required
def autos_home(request):
    user = request.user

    if Auto.objects.filter(owner_id=user.id).exists():
        autos = Auto.objects.get(owner_id=user.id)
    else:
        autos = []
    data = {
        'autos': autos
    }
    return render(request, 'autos/autos_home.html', data)


@login_required
class AutoDetailView(DetailView):
    model = Auto
    template_name = 'autos/details_view.html'
    context_object_name = 'auto'


@login_required
class AutoUpdateView(UpdateView):
    model = Auto
    template_name = 'autos/create_auto.html'

    form_class = AutosForm


@login_required
class AutoDeleteView(DeleteView):
    model = Auto
    success_url = '/autos'
    template_name = 'autos/delete_auto.html'


@login_required
def create_auto(request):
    error = ''
    if request.method == 'POST':
        form = AutosForm(request.POST, request.FILES)
        if form.is_valid():
            new_auto = form.save(commit=False)
            new_auto.owner_id = request.user.id
            new_auto.save()
            return redirect('/autos')
        else:
            error = 'Форма заполнена некорректно'
    form = AutosForm(request.POST, request.FILES)

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'autos/create_auto.html', data)
