from django.contrib import admin
from django.urls import path, include
from Galeria import views

urlpatterns = [
    path('admin', admin.site.urls), 
    path('', views.inicio, name="Inicio"),
    path('artistas', views.artistas, name="artista"),
    path('avaluadores', views.avaluadores, name="avaluador"),
    path('obras', views.obras, name="obra"),
    path('buscar/', views.buscar),

]