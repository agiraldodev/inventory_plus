from django.shortcuts import render, get_object_or_404
from .models import Equipo

def home(request):
    equipos = Equipo.objects.all()
    return render(request, 'inventario/home.html', {'equipos': equipos})

def equipo_detail(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    mantenimientos = equipo.mantenimientos.all()
    return render(request, 'inventario/equipo_detail.html', {'equipo': equipo, 'mantenimientos': mantenimientos})