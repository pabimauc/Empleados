from django.db import models
#
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'
        ordering = ['habilidad']
        #unique_together = ('habilidad')

    def __str__(self):
        return str(self.id) + '-' + self.habilidad



TRABAJO_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro'),
)
class Empleado(models.Model):
    """ Modelo para tabla Empleado """
    nombre = models.CharField('Nombres', max_length=60)
    apellidos = models.CharField('Apellidos', max_length=60)
    nombre_completo = models.CharField('Nombre Completo', max_length=120, blank=True)
    trabajo = models.CharField('Trabajo', max_length=1, choices=TRABAJO_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Registrar Empleado'
        verbose_name_plural = 'Registrar Empleados'
        ordering = ['nombre']
        unique_together = ('nombre', 'apellidos')

    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellidos