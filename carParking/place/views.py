from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Place
from .forms import PlacesForm
from django.views.generic import DetailView, UpdateView, DeleteView

from auto.models import Auto


def places_home(request):
    if request.method == 'POST':
        place_number = request.POST.get('place_number')
        return redirect('choose_place', place_number=place_number)
    places = Place.objects.all()

    data = {
        'places': places
    }
    return render(request, 'places/places_home.html', data)


def choose_car(request, place_number):
    if request.method == 'POST':
        place = Place.objects.get(number=place_number)
        place.auto_id = request.POST.get('car_id')
        auto = Auto.objects.get(id=request.POST.get('car_id'))
        auto.isParked = True
        auto.save()
        place.save()
        redirect('/places')
    user = request.user
    autos = Auto.objects.filter(owner_id=user.id)
    data = {
        'autos': autos,
        'place_number': place_number
    }
    return render(request, 'places/choose_car.html', data)


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/details_view.html'
    context_object_name = 'place'


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = 'places/create_place.html'

    form_class = PlacesForm


class PlaceDeleteView(DeleteView):
    model = Place
    success_url = '/places'
    template_name = 'places/delete_place.html'


@login_required
def create_place(request):
    error = ''
    if request.method == 'POST':
        form = PlacesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/places')
        else:
            error = 'Форма заполнена некорректно'
    form = PlacesForm(request.POST)

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'places/create_place.html', data)
