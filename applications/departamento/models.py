from hashlib import md5
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    nombre_corto = models.CharField('Nombre Corto', max_length=20)
    anulado = models.BooleanField('Anulado', default=False)
    

    class Meta:
        verbose_name = 'Departamentos de la Empresa'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['nombre']
        unique_together = ('nombre', 'nombre_corto')

    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.nombre_corto
