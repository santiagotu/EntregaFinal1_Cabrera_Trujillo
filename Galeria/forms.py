from django import forms

from Galeria.models import Artista, Obra

class ArtistaFormulario(forms.Form):
    nombre = forms.CharField()
    estilo = forms.IntegerField()
    pass

class ObraFormulario(forms.Form):   
    nombre = forms.CharField(max_length=60)
    fecha = forms.DateField()
    precio = forms.FloatField()
    artista1 = forms.ModelMultipleChoiceField(queryset=Artista.objects.all())
    #artista = forms.ForeignKey(Artista, on_delete=forms.CASCADE, null=True)
    pass

class AvaluadorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=60)
    fecha = forms.DateField()


    