from django.urls import path
from . import views

urlpatterns = [
    path('', views.places_home, name='places_home'),
    path('create/', views.create_place, name='create_place'),
    path('choose/<int:place_number>', views.choose_car, name='choose_place'),
    path('<int:pk>', views.PlaceDetailView.as_view(), name='place_detail'),
    path('<int:pk>/update', views.PlaceUpdateView.as_view(), name='place_update'),
    path('<int:pk>/delete', views.PlaceDeleteView.as_view(), name='place_delete')
]
