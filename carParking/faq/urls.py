from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_home, name='faq_home'),
    path('<int:pk>', views.FaqDetailView.as_view(), name='faq_detail'),
]
