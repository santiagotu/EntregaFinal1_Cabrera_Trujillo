from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=40)
    estilo = models.CharField(max_length=40)

class Obra(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    precio = models.FloatField()

class Avaluador(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()