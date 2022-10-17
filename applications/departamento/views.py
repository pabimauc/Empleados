from os import defpath
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento

from .forms import NewDepartamentoForm


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('************Estamos en el form valid************')

        depa = Departamento(
            nombre=form.cleaned_data['departamento'],
            nombre_corto=form.cleaned_data['nombre_corto']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            nombre = nombre,
            apellidos = apellidos,
            trabajo='1',
            departamento=depa 
        )

        return super(NewDepartamentoView, self).form_valid(form)


