from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    # path('register/', views.RegisterFormView.as_view(), name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
