from django.db import models
from datetime import date
from django.urls import reverse


class Artista(models.Model):
    nombre = models.CharField(max_length=60)
    estilo = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre}"

    def get_absolute_url(self):
        return reverse('mostrar_artista', args=(str(self.id)))


class Obra(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField(default=date.today)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="img_obras/")
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha: {self.fecha} - Precio: {self.precio} {self.imagen}"

    def get_absolute_url(self):
        return reverse('mostrar_obra', args=(str(self.id)))


class Avaluador(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField(default=date.today)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha: {self.fecha}"

    def get_absolute_url(self):
        return reverse('mostrar_avaluador', args=(str(self.id)))
