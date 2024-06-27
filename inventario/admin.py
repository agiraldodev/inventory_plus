from django.contrib import admin
from django.db import models
from django.forms import SelectMultiple
from .models import Equipo, Mantenimiento, TipoMantenimiento

admin.site.site_header = 'Control de Mantenimientos de Equipos'
admin.site.index_title = 'InventoryPlus | Panel administrativo'

class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'ubicacion'
    )


class MantenimientoAdmin(admin.ModelAdmin):
    list_display = (
        'fechaHoraMantenimiento',
        'equipoID'
    )
    filter_horizontal = ('tiposMantenimiento',)  # Agregar filtros horizontales para un mejor manejo

    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={
            'class': 'admin-select',
            'style': 'height: auto;',
            'size': 10,
        })},
    }

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.save()  # Guardar el objeto Mantenimiento primero

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Mantenimiento, MantenimientoAdmin)