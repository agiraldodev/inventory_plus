from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipo/<int:equipo_id>/', views.equipo_detail, name='equipo_detail'),
]
