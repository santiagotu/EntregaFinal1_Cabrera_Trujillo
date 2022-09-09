from http.client import HTTPResponse
from django.shortcuts import render
from Galeria.forms import ArtistaFormulario, AvaluadorFormulario, ObraFormulario
from Galeria.models import Obra, Artista, Avaluador

def inicio(request):
    return render(request, "Galeria/inicio.html", context={})
	
def artista(request):
      artista = Artista(nombre="Giovanni Paolo Panini", estilo="Pintura neoclásica")
      #artista.save()
      artista1 = Artista.objects.create(nombre="Edvard Munch", estilo="Expresionismo")
      #artista1.save()
      artista2 = Artista.objects.create(nombre="Robert Delaunay", estilo="Abstracción")
      #artista2.save()
      artistas_list = Artista.objects.all()
      context = {'artista': artista,
                 'artista1': artista1,
                 'artista2': artista2}
      return render(request, 'Galeria/artistas.html', {'artistas_list': artistas_list})     

def obras(request):
    artistas = Artista.objects.all()

    obra1 = Obra.objects.create(nombre="King Oliver", fecha="1958-01-01", precio=250000, artista=artistas[0])
    #obra1.save()
    obra2 = Obra.objects.create(nombre="Número 16", fecha="1949-01-01", precio=32000000, artista=artistas[1])
    #obra2.save()
    obra3 = Obra.objects.create(nombre="Naranja, rojo y amarillo", fecha="1961-01-01", precio=86500000, artista=artistas[2])
    #obra3.save()    
    obras_list = Obra.objects.all()
    context = {'obra1': obra1,
               'obra2': obra2,
               'obra3': obra3}
    return render(request, 'Galeria/obras.html', {'obras_list': obras_list})

def avaluador(request):
    obras = Obra.objects.all()
    
    avaluador1 = Avaluador.objects.create(nombre="Mateo Perez", fecha="2022-01-01", obra=obras[1])
    #avaluador1.save()
    avaluador2 = Avaluador.objects.create(nombre="Rosario Fuentes", fecha="2021-01-01", obra=obras[2])
    #avaluador2.save()
    avaluador3 = Avaluador.objects.create(nombre="Ana Fawk", fecha="2012-01-01", obra=obras[3])
    #avaluador3.save()
    avaluadores_list = Obra.objects.all()
    context = {'avaluador1': avaluador1,
               'avaluador2': avaluador2,
               'avaluador3': avaluador3}
    return render(request, 'Galeria/avaluadores.html', {'avaluadores_list': avaluadores_list})

def artistas_crear(request):
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

def obras_crear(request):
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

def avaluadores_crear(request):
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
            artista = Artista.objects.filter(estilo__icontains=estilo)
            return render(request, "Galeria/inicio.html", {"Artista":artista, "estilo":estilo})
      else:
            respuesta = "No enviaste datos"
            return HTTPResponse(respuesta)