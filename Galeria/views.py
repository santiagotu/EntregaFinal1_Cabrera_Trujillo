from http.client import HTTPResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Galeria.models import Artista, Avaluador, Obra
from .forms import FormBusquedaObras, ObraFormulario, FormBusquedaArtistas, ArtistaFormulario, FormBusquedaAvaluadores, AvaluadorFormulario
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
    ultimos_cinco_artistas = Artista.objects.all().order_by('-id')[:5]
    return render(request, "inicio.html", context={})


def acerca_de_nosotros(request):
    return render(request, 'about.html')


def paginas(request):
    return render(request, 'pages.html')

###############################################################################

class ListadoArtistas(ListView):
    model = Artista
    template_name = 'listado_artistas.html'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaArtistas()
        return context


class CrearArtista(LoginRequiredMixin, CreateView):
    model = Artista
    form_class = ArtistaFormulario
    template_name = 'crear_artistas.html'
    success_url = '/listado_artistas'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditarArtista(LoginRequiredMixin, UpdateView):
    model = Artista
    form_class = ArtistaFormulario
    template_name = 'listado_artistas'
    success_url = '/listado_artistas'


class EliminarArtista(LoginRequiredMixin, DeleteView):
    model = Artista
    template_name = 'artistas.html'
    success_url = '/listado_artistas'


class MostrarArtista(DetailView):
    model = Artista
    template_name = '/mostrar_artista.html'

###############################################################################

class ListadoObras(ListView):
    model = Obra
    template_name = 'listado_obras.html'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaObras()
        return context


class CrearObra(LoginRequiredMixin, CreateView):
    model = Obra
    form_class = ObraFormulario
    template_name = 'crear_obras.html'
    success_url = '/listado_obras'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditarObra(LoginRequiredMixin, UpdateView):
    model = Obra
    form_class = ObraFormulario
    template_name = 'listado_obras'
    success_url = '/listado_obras'


class EliminarObra(LoginRequiredMixin, DeleteView):
    model = Obra
    template_name = 'obras.html'
    success_url = '/listado_obras'


class MostrarObra(DetailView):
    model = Obra
    template_name = 'mostrar_obra.html'

###############################################################################

class ListadoAvaluadores(ListView):
    model = Avaluador
    template_name = 'listado_avaluadores.html'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaAvaluadores()
        return context


class CrearAvaluador(LoginRequiredMixin, CreateView):
    model = Avaluador
    form_class = AvaluadorFormulario
    template_name = 'crear_avaluadores.html'
    success_url = '/listado_avaluadores'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditarAvaluador(LoginRequiredMixin, UpdateView):
    model = Avaluador
    form_class = AvaluadorFormulario
    template_name = 'listado_avaluadores'
    success_url = '/listado_avaluadores'


class EliminarAvaluador(LoginRequiredMixin, DeleteView):
    model = Avaluador
    template_name = 'avaluadores.html'
    success_url = '/listado_avaluadores'


class MostrarAvaluador(DetailView):
    model = Avaluador
    template_name = '/mostrar_avaluador.html'
