from django.contrib import admin
from django.urls import path, include
from Galeria import views

urlpatterns = [
    path('admin', admin.site.urls), 
    path('', views.inicio, name="Inicio"),
    path('artistas', views.artista, name="artista"),
    path('avaluadores', views.avaluador, name="avaluador"),
    path('obras', views.obra, name="obra")

]