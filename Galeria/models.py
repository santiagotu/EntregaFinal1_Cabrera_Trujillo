from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=60)
    estilo = models.CharField(max_length=60)

    def __str__(self):
        return f"Nombre: {self.nombre} - Estilo: {self.estilo}"

class Obra(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()
    precio = models.FloatField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha: {self.estilo} - Precio: {self.precio}"    

class Avaluador(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField()
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha: {self.fecha}"