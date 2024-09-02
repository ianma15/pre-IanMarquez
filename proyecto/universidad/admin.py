from django.contrib import admin
from .models import Estudiante, Materia, Solicitud

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni')
    search_fields = ('nombre', 'apellido', 'dni')
    ordering = ('apellido', 'nombre')

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'turno_de_cursada', 'ofertada')
    list_filter = ('ofertada',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'estado', 'fecha_de_solicitud')
    list_filter = ('estado', 'fecha_de_solicitud')
    search_fields = ('estudiante__nombre', 'materia__nombre')
    ordering = ('-fecha_de_solicitud',)
    date_hierarchy = 'fecha_de_solicitud'