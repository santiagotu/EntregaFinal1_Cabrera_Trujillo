from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=60)
    estilo = models.CharField(max_length=60)

class Obra(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()
    precio = models.FloatField()

class Avaluador(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()