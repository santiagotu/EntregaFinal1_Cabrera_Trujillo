from django.contrib import admin
from django.urls import path, include
from Galeria.views import inicio, artista, avaluador, obra

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('inicio/', inicio, name="inicio"),
    path('artistas/', artista, name="artista"),
    path('avaluadores/', avaluador, name="avaluador"),
    path('obras/', obra, name="obra"),
    #path('Galeria/', include('Galeria.urls')),

]