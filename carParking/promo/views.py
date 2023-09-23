from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Promo
from main.models import Profile


@login_required
def promos_home(request):
    promos = Promo.objects.all()
    data = {
        'promos': promos
    }
    if request.method == "POST":
        if Promo.objects.filter(promo=request.POST.get('promo_field')).exists():
            promo = Promo.objects.get(promo=request.POST.get('promo_field'))
            if promo.isActive:
                profile = Profile.objects.get(user_id=request.user.id)
                profile.money += promo.prize
                profile.save()
                promo.isActive = False
                promo.save()
                data['message'] = f'Вы успешно использовали промокод и получили {promo.prize} руб.'
            else:
                data['message'] = 'Извините. Данный промокод уже использован.'
        else:
            data['message'] = 'Извините. Данного промокода не существует.'

    return render(request, 'promo/promos_home.html', data)
