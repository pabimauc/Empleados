from multiprocessing import context
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    
    
)


from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5
    ordering = 'apellidos'
    context_object_name='empleados'
    
    def get_queryset(self): 
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'apellidos'
    context_object_name='empleados'
    model = Empleado
    

class ListByAreaEmplados(ListView):
    template_name = 'persona/list_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__nombre_corto = area
        )
        return lista

    
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self): 
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            nombre = palabra_clave
        )
        return lista


class ListHabilidadesEmpleados(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidad'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3
        )
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalle_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'



class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado 
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.nombre_completo = empleado.nombre + ' ' + empleado.apellidos
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'nombre',
        'apellidos',
        'trabajo',
        'departamento',
        'habilidades'
    ]

    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('************METODO POST***************')
        print('***************************')
        print(request.POST)
        print(request.POST['nombre'])
        return super().post(request, *args, **kwargs)
        
        
    def form_valid(self, form):
        print('************METODO form valid***************')
        print('***************************')
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')


        
    
