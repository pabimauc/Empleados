from audioop import minmax
from xml.dom import minidom
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo

