# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from comun.models import Rol, Cooperativa, Usuario


class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    ordering = ('id',)

class CooperativaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ciudad')
    ordering = ('id',)

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('foto','descripcion','telefono','direccion', 'get_rol')
    def get_rol(self, obj):
        return obj.rol.nombre
# Register your models here.
admin.site.register(Rol, RolAdmin),
admin.site.register(Cooperativa, CooperativaAdmin),
admin.site.register(Usuario,UsuarioAdmin)
