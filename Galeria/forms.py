from datetime import datetime
from django import forms
from .models import Artista, Avaluador, Obra
from bootstrap_datepicker_plus.widgets import DatePickerInput


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class ArtistaFormulario(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estilo': forms.TextInput(attrs={'class': 'form-control'})
        }


class ObraFormulario(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ('nombre', 'fecha', 'precio', 'artista')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': DatePickerInput(format='%Y-%m-%d'),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.Select(attrs={'class': 'form-control'}),
        }


class AvaluadorFormulario(forms.ModelForm):
    class Meta:
        model = Avaluador
        fields = ('nombre', 'fecha')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': DatePickerInput(format='%Y-%m-%d'),
            'obra': forms.Select(attrs={'class': 'form-control'}),
        }


class FormBusquedaArtistas(forms.Form):
    nombre = forms.CharField(max_length=60, required=False)


class FormBusquedaObras(forms.Form):
    nombre = forms.CharField(max_length=60, required=False)


class FormBusquedaAvaluadores(forms.Form):
    nombre = forms.CharField(max_length=60, required=False)
