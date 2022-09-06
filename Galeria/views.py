from http.client import HTTPResponse
from django.shortcuts import render
from Galeria.forms import ArtistaFormulario, AvaluadorFormulario, ObraFormulario
from Galeria.models import Obra, Artista, Avaluador

def inicio(request):
    return render(request, "Galeria/inicio.html", context={})
	
def obras(request):
      return render(request, "Galeria/obras.html")	

def artista(request):
      artista = Artista(nombre=" Giovanni Paolo Panini", estilo="Pintura neoclásica")
      artista1 = Artista.objects.create(nombre="Edvard Munch", estilo="Expresionismo")
      artista2 = Artista.objects.create(nombre="Robert Delaunay", estilo="Abstracción")
      artista.save()
      context = {'artista': artista,
                 'artista1': artista1,
                 'artista2': artista2}
      return render(request, 'Galeria/artistas.html', context)

def obra(request):
    artistas = Artista.objects.get(nombre=request.nombre)

    obra1 = Obra.objects.create(nombre="King Oliver", fecha="1958-01-01", precio=250000, artistas=request.nombre)
    obra2 = Obra.objects.create(nombre="Número 16", fecha="1949-01-01", precio=32000000, artistas=request.nombre)
    obra3 = Obra.objects.create(nombre="Naranja, rojo y amarillo", fecha="1961-01-01", precio=86500000, artistas=request.nombre)
    obra.save()    
    context = {'obra1': obra1,
               'obra2': obra2,
               'obra3': obra3}
    return render(request, 'Galeria/obras.html', context) 

def avaluador(request):
    obras = Obra.objects.get(nombre=request.nombre)
    
    avaluador1 = Avaluador.objects.create(nombre="Mateo Perez", fecha="2022-01-01", obras=request.nombre)
    avaluador2 = Avaluador.objects.create(nombre="Rosario Fuentes", fecha="2021-01-01", obras=request.nombre)
    avaluador3 = Avaluador.objects.create(nombre="Ana Fawk", fecha="2012-01-01", obras=request.nombre)
    avaluador.save()
    context = {'avaluador1': avaluador1,
               'avaluador2': avaluador2,
               'avaluador3': avaluador3}
    return render(request, 'Galeria/avaluadores.html', context)  

#
#
def artistas(request):
      if request.method == 'POST':
            miFormulario = ArtistaFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  artista = Artista (nombre=informacion['nombre'], estilo=informacion['estilo']) 
                  artista.save()
                  return render(request, "Galeria/inicio.html") 
      else: 
            miFormulario= ArtistaFormulario()
      return render(request, "Galeria/artistas.html", {"miFormulario":miFormulario})    

def obra(request):
      if request.method == 'POST':
            miFormulario = ObraFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  obra = Obra (nombre=informacion['nombre'], fecha=informacion['fecha'], precio=informacion['precio'], artista=informacion['artista.nombre']) 
                  obra.save()
                  return render(request, "Galeria/inicio.html") 
      else: 
            miFormulario= ObraFormulario()
      return render(request, "Galeria/obras.html", {"miFormulario":miFormulario})   

def avaluadores(request):
      if request.method == 'POST':
            miFormulario = AvaluadorFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  avaluador = Avaluador (nombre=informacion['nombre'], fecha=informacion['fecha'], precio=informacion['precio']) 
                  avaluador.save()
                  return render(request, "Galeria/inicio.html") 
      else: 
            miFormulario= AvaluadorFormulario()
      return render(request, "Galeria/avaluadores.html", {"miFormulario":miFormulario})    

def buscar(request):
      if  request.GET["estilo"]:
	      #respuesta = f"Estoy buscando el estilo: {request.GET['estilo'] }" 
            estilo = request.GET['estilo'] 
            artistas = Artista.objects.filter(estilo__icontains=estilo)
            return render(request, "Galeria/inicio.html", {"Artista":artista, "estilo":estilo})
      else:
            respuesta = "No enviaste datos"
            return HTTPResponse(respuesta)