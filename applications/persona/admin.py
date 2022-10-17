from django.contrib import admin

from applications.departamento.models import Departamento
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellidos',
        'departamento',
        'trabajo',
        'nombre_completo',
    )
    #
    def nombre_completo(self, obj):
        print(obj.nombre)
        return obj.nombre + ' ' + obj.apellidos
    #
    search_fields = ('nombre',)
    list_filter = ('trabajo', 'habilidades')
    #
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)