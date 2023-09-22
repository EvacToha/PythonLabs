from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('contacts/', views.contacts, name='contacts'),
    path('openings/', views.openings, name='openings')
]
