from django.urls import path
from . import views

urlpatterns = [
    path('', views.autos_home, name='autos_home'),
    path('create/', views.create_auto, name='create_auto'),
    path('<int:pk>', views.AutoDetailView.as_view(), name='auto_detail'),
    path('<int:pk>/update', views.AutoUpdateView.as_view(), name='auto_update'),
    path('<int:pk>/delete', views.AutoDeleteView.as_view(), name='auto_delete')
]
