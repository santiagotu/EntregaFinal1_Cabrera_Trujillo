from http.client import HTTPResponse
from django.shortcuts import render
from Galeria.forms import ArtistaFormulario, AvaluadorFormulario, ObraFormulario
from Galeria.models import Obra, Artista, Avaluador

def inicio(request):
    return render(request, "Galeria/inicio.html", context={})
	
def artistas2(request):
      artista = Artista(nombre="Giovanni Paolo Panini", estilo="Pintura neoclásica")
      #artista.save()
      artista1 = Artista.objects.create(nombre="Edvard Munch", estilo="Expresionismo")
      #artista1.save()
      artista2 = Artista.objects.create(nombre="Robert Delaunay", estilo="Abstracción")
      #artista2.save()
      artistas_list = Artista.objects.all()
      context = {'artista': artista, 'artista1': artista1, 'artista2': artista2}
      return render(request, 'Galeria/artistas2.html', {'artistas_list': artistas_list})     

####################################################################### 
def artistas(request):
    """View for artistas page."""
    # Para buscar si el usuario tiene avatar
    #try:
        #avatar = Avatar.objects.get(user=request.user.id)
        #avatar = avatar.avatar.url
    #except:
        #avatar = ''

    # Defino variable conteniendo todos los artistas ordenados de mas nuevo a mas antiguo
    artistas = Artista.objects.all()
    artistas_list = Artista.objects.all()

    # Para buscar artistas por estilo
    style = request.GET.get('estilo')
    if style:
        artistas = Artista.objects.filter(style__icontains=style)
        context = {
            'title': 'artistas',
            'style': style,
            'search': 'Buscar por estilo',
            'artistas': artistas,
        }
        return render(request, 'Galeria/artistas.html', artistas)  
    
    else:
        # Listar todos los artistas
        context = {
            'artistas': artistas,
            'title': 'artistas',
            'subtitle': '¡El listado completo de nuestros artistas!',
            'search': 'Buscar por estilo',
        }
        return render(request, 'Galeria/artistas.html', {'artistas_list': artistas_list}) 
#######################################################################        
""" def artistas_crear(request):
      if request.method == 'Artista':
            miFormulario = ArtistaFormulario(request.Artista) 
            print(miFormulario)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data
                  artista = Artista (nombre=informacion['nombre'], estilo=informacion['estilo']) 
                  #artista.save()
                  #return render(request, "Galeria/inicio.html") 
      else: 
            miFormulario= ArtistaFormulario()
      return render(request, "Galeria/artistas.html", context)   """
      

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

def avaluadores(request):
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
 

def obras_crear(request):
      if request.method == 'Artista':
            miFormulario = ObraFormulario(request.Artista)
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
      if request.method == 'Artista':
            miFormulario = AvaluadorFormulario(request.Artista) 
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