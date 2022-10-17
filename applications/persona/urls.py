from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('', 
        views.InicioView.as_view(),
        name = 'inicio'
    ),
    path(
        'listar-todo-empleado/', 
        views.ListAllEmpleados.as_view(),
        name = 'empleados_all'
    ),
    path(
        'listar-empleado-area/<shorname>/',
        views.ListByAreaEmplados.as_view(),
        name = 'lista_areas'  
    ),
    path(
        'listar-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name = 'empleados_admin'
    ),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view(),
    ),
    path('listar-habilidades-empleado/', views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>',
        views.EmpleadoDetailView.as_view(),
        name = 'detalle_empleado'
    ),
    path(
        'crear-empleado/',
         views.EmpleadoCreateView.as_view(),
         name='empleado_add'
    ),
    path('success/', views.SuccessView.as_view(), name = 'correcto'),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name = 'modificado'),

    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name = 'eliminado'),
]
