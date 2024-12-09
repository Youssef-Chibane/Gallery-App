from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('show/<int:pk>', views.show_image, name='Show'),
    path('add/', views.add_image, name='Add'),
]
