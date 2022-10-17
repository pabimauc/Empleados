from re import template
from venv import create
from django.shortcuts import render
#
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
#
from .models import Prueba

from .form import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'  



    
class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listanumeros'
    queryset = ['0', '10', '20', '30']
    

class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html" 
    model = Prueba
    form_class = PruebaForm
    success_url = '/'