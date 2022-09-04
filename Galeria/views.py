from django.shortcuts import render
from Galeria.forms import ArtistaFormulario, AvaluadorFormulario, ObraFormulario
from Galeria.models import Obra, Artista, Avaluador

def inicio(request):
    return render(request, "inicio.html", context={})

def artista(request):
    artista1 = Artista.objects.create(nombre=" Giovanni Paolo Panini", estilo="Pintura neoclásica")
    artista2 = Artista.objects.create(nombre="Edvard Munch", estilo="Expresionismo")
    artista3 = Artista.objects.create(nombre="Robert Delaunay", estilo="Abstracción")
    context = {'artista1': artista1,
               'artista2': artista2,
               'artista3': artista3}
    return render(request, 'artistas.html', context)

def obra(request):
    artistas = Artista.objects.get(nombre=request.nombre)

    obra1 = Obra.objects.create(nombre="King Oliver", fecha="1958-01-01", precio=250000, artistas=request.nombre)
    obra2 = Obra.objects.create(nombre="Número 16", fecha="1949-01-01", precio=32000000, artistas=request.nombre)
    obra3 = Obra.objects.create(nombre="Naranja, rojo y amarillo", fecha="1961-01-01", precio=86500000, artistas=request.nombre)
    
    context = {'obra1': obra1,
               'obra2': obra2,
               'obra3': obra3}
    return render(request, 'obras.html', context)    

def avaluador(request, obra1, obra2, obra3):

    obra1 = Artista.objects.get(nombre=request.obra)
    obra2 = Artista.objects.get(nombre=request.obra)
    obra3 = Artista.objects.get(nombre=request.obra)

    avaluador1 = Avaluador.objects.create(nombre="Mateo Perez", fecha="2022-01-01", obra=obra1)
    avaluador2 = Avaluador.objects.create(nombre="Rosario Fuentes", fecha="2021-01-01", obra=obra2)
    avaluador3 = Avaluador.objects.create(nombre="Ana Fawk", fecha="2012-01-01", obra=obra3)
    context = {'avaluador1': avaluador1,
               'avaluador2': avaluador2,
               'avaluador3': avaluador3}
    return render(request, 'avaluadores.html', context)  


def artistas(request):
      if request.method == 'POST':
            miFormulario = ArtistaFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  artista = Artista (nombre=informacion['nombre'], estilo=informacion['estilo']) 
                  artista.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= ArtistaFormulario()
      return render(request, "artistas.html", {"miFormulario":miFormulario})    

def obras(request):
      if request.method == 'POST':
            miFormulario = ObraFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  obra = Artista (nombre=informacion['nombre'], fecha=informacion['fecha'], precio=informacion['precio']) 
                  obra.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= ObraFormulario()
      return render(request, "obras.html", {"miFormulario":miFormulario})    

def avaluadores(request):
      if request.method == 'POST':
            miFormulario = AvaluadorFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  avaluador = Avaluador (nombre=informacion['nombre'], fecha=informacion['fecha'], precio=informacion['precio']) 
                  avaluador.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= ObraFormulario()
      return render(request, "avaluadores.html", {"miFormulario":miFormulario})    