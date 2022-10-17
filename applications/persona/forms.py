from tkinter import Widget
from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = (
            'nombre',
            'apellidos',
            'trabajo',
            'departamento',
            'imagen',
            'habilidades',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
