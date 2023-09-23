from django.urls import path
from . import views

urlpatterns = [
    path('', views.promos_home, name='promos_home'),
]
