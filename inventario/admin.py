from django.contrib import admin
from .models import Equipo, Mantenimiento

admin.site.site_header = 'Control de Mantenimientos de Equipos'
admin.site.index_title = 'InventoryPlus | Panel administrativo'

admin.site.register(Equipo)
admin.site.register(Mantenimiento)